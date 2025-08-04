import json
import boto3

# Initialize the DynamoDB resource
dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('Tasks')

def lambda_handler(event, context):
    try:
        response = table.scan()
        items = response.get('Items', [])

        # Return the list of tasks
        return {
            'statusCode': 200,
            'body': json.dumps(items)
        }

    except Exception as e:
        # Return error if the scan fails
        return {
            'statusCode': 500,
            'body': json.dumps({'error': str(e)})
        }
