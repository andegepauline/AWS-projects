import json            # For parsing and returning JSON data
import uuid            # For generating unique task IDs
import boto3           # AWS SDK to interact with DynamoDB
from datetime import datetime  # To add timestamps

# Create a DynamoDB resource using the default credentials
dynamodb = boto3.resource('dynamodb')

# Connect to the 'Tasks' table
table = dynamodb.Table('Tasks')

def lambda_handler(event, context):
    # Parse the JSON body from the HTTP request
    data = json.loads(event['body'])

    # Generate a unique ID for the new task
    task_id = str(uuid.uuid4())

    # Build the task to insert into DynamoDB
    item = {
        'id': task_id,
        'title': data['title'],                        
        'description': data.get('description', ''),     
        'status': data.get('status', 'pending'),         
        'created_at': datetime.utcnow().isoformat()     
    }

    # Put the item into the DynamoDB table
    table.put_item(Item=item)

    # Return a success response
    return {
        'statusCode': 201,
        'body': json.dumps({
            'message': 'Task created',
            'task': item
        })
    }
