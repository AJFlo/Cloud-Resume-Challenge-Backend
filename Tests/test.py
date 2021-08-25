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

LambdaName= "sam-app-StartWithSamFunction02-HLW6Sk6U2FAH"

response = lambda_client.invoke(FunctionName=LambdaName)

assert response > 0

