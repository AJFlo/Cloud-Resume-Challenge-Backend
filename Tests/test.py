import unittest
import boto3
import botocore
import json
import typing

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


# Invoke your Lambda function as you normally usually do. The function will run
# locally if it is configured to do so

def invokeLambdaFunction(*, functionName:str=None, payload:typing.Mapping[str, str]=None):
    if  functionName == None:
        raise Exception('ERROR: functionName parameter cannot be NULL')
    payloadStr = json.dumps(payload)
    payloadBytesArr = bytes(payloadStr, encoding='utf8')
    client = boto3.client('lambda')
    response = client.invoke(
        FunctionName=functionName,
        InvocationType="RequestResponse",
        Payload=payloadBytesArr
    )
    return response

assert invokeLambdaFunction(functionName="StartWithSamFunction02", payload={"ping":0123})
response = lambda_client.invoke(FunctionName="StartWithSamFunction02")

# Verify the response
assert response == int(response)
