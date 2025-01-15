import boto3
import logging
from botocore.exceptions import ClientError
import pprint
from rich import print

# Initialize logging
logging.basicConfig(filename = 'obj_ver.log',filemode= 'w', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Initialize a session
session = boto3.Session()

def list_object_version(bucket_name):
    try:
        s3_client = session.client('s3')
        response = s3_client.list_object_versions(
        Bucket= bucket_name   
)   
        print(response)
    except ClientError as e:
        logging.error(f" ClientError occured: {e}")
        return False
    return True

list_object_version('natebucket007')