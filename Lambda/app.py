import json
import boto3
import os
from decimal import Decimal

dynamodb = boto3.resource("dynamodb")
ddbTableName = os.environ["databaseName"] 
table = dynamodb.Table(ddbTableName)
Key = {"Visitor_Count": { "N" : "0" }}

        
def handler(event, context):
           # Update item in table or add if doesn't exist
    ddbResponse = table.update_item(
        Key={"id": "Visitor_Count"},
        UpdateExpression= "ADD Visitor_Count :val",
        ExpressionAttributeValues={":val": Decimal(1)},
        ReturnValues="UPDATED_NEW",
    )

    # Format dynamodb response into variable
    responseBody = json.dumps({"Visitor_Count": int(ddbResponse["Attributes"]["Visitor_Count"])})

    # Create api response object
    apiResponse = {"isBase64Encoded": False, "statusCode": 200,'headers': {
            'Access-Control-Allow-Headers': 'Content-Type',
            'Access-Control-Allow-Origin': 'https://antoniojflores.com',
            'Access-Control-Allow-Methods': 'OPTIONS, POST, GET'
        },"body": responseBody}

    # Return api response object
    return apiResponse

