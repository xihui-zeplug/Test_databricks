
import boto3
import base64
from botocore.exceptions import ClientError


def get_secret(name_secret):
    secret_name = name_secret
    region_name = "eu-west-3"

   # Create a Secrets client
    session = boto3.session.Session(
        profile_name = 'zeplug-prod'
    )

    client = session.client(
        service_name='secretsmanager',
        region_name=region_name)
    get_secret_value_response = client.get_secret_value(
        SecretId=secret_name)
    secret = get_secret_value_response['SecretString']
    return secret

