import json
import boto3

# Connect to DynamoDB
dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('Tasks')

def lambda_handler(event, context):
    task_id = event['pathParameters']['id']

    try:
        # Delete the item with the given ID
        table.delete_item(Key={'id': task_id})

        return {
            'statusCode': 200,
            'body': json.dumps({'message': 'Task deleted successfully'})
        }

    except Exception as e:
        return {
            'statusCode': 500,
            'body': json.dumps({'error': str(e)})
        }
