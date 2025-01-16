import boto3
import logging
from botocore.exceptions import ClientError
from rich import print

# initialize a session 
session = boto3.Session()

# initialize s3 client
s3_client = session.client('s3')

# Logging configuration
logging.basicConfig(filemode = 'w',level=logging.INFO, format ='%(asctime)s - %(levelname)s - %(messages)s')


def list_bucket_objects(bucket_name):
    try:
        s3_client = session.client('s3')
        response = s3_client.list_objects_v2(
            Bucket = bucket_name   
        )

        print(response)
    except ClientError as e:
        logging.error(e)
        return False
    return True

list_bucket_objects('mys3bucketoto3')