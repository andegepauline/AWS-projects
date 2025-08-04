import json
import boto3

# Initialize the DynamoDB resource
dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('Tasks')

def lambda_handler(event, context):
    # Extract the 'id' path parameter from the API Gateway request
    task_id = event['pathParameters']['id']

    try:
        # Retrieve the task from DynamoDB using the ID
        response = table.get_item(Key={'id': task_id})
        item = response.get('Item')

        # If item not found, return 404
        if not item:
            return {
                'statusCode': 404,
                'body': json.dumps({'message': 'Task not found'})
            }

        # Return the task details
        return {
            'statusCode': 200,
            'body': json.dumps(item)
        }

    except Exception as e:
        # Return internal server error if something fails
        return {
            'statusCode': 500,
            'body': json.dumps({'error': str(e)})
        }
