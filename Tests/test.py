import unittest
import boto3
import botocore
import json
import typing
import requests
from requests.auth import HTTPDigestAuth

running_locally = False

if running_locally:

    # Create Lambda SDK client to connect to appropriate Lambda endpoint
    lambda_client = boto3.client('lambda',
        region_name="us-west-2",
        endpoint_url="http://127.0.0.1:3001",
        use_ssl=False,
        verify=False,
        config=botocore.client.Config(
            signature_version=botocore.UNSIGNED,
            read_timeout=1,
            retries={'max_attempts': 0},
        )
    )
else:
    lambda_client = boto3.client('lambda')
    
    
ApiUrl= "https://h2r98egvbi.execute-api.us-east-2.amazonaws.com/Prod/Visitor_Count/"
Key = "Visitor_Count"
    # It is a good practice not to hardcode the credentials. So ask the user to enter credentials at runtime
myResponse = requests.get(ApiUrl, verify=True)
#print (myResponse.status_code)
def IsInteger(num):
    assert num==int(num)

def IsPositive(num):
    assert num>0
# For successful API call, response code will be 200 (OK)
if(myResponse.ok):
    # Loading the response data into a dict variable
    # json.loads takes in only binary or string variables so using content to fetch binary content
    # Loads (Load String) takes a Json file and converts into python data structure (dict or list, depending on JSON)
    jData = json.loads(myResponse.content)
    print(jData)
    print(jData[0])
    print(jData[0][Key])
    V=jData[0][Key]
if(IsInteger(V) and IsPositive(V)):
    
    print (myResponse.status_code)
    
       
    #return True
    
  # If response code is not ok (200), print the resulting http error code with description
    


# Invoke your Lambda function as you normally usually do. The function will run
# locally if it is configured to do so




