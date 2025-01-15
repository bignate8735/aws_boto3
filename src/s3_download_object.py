import os
import boto3
import logging
from botocore.exceptions import ClientError
from rich import print

# Initialize session
session =boto3.Session()

# Initialize logging
logging.basicConfig(filename= 'get_obj.log', filemode= 'w',level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')


def download_file_from_s3(bucket_name, s3_object_key, local_file_path):
    try:
        s3_client = session.client('s3')
        response = s3_client.download_file(
            Bucket = bucket_name,
            Key = s3_object_key, 
            Filename = local_file_path
        )
        print(f" File downloaded succcessfully: {response}")
    except ClientError as e:
        logging.error(e)  
        return False
    return True
    


download_file_from_s3('mys3bucketoto3','african_crises.csv','/Users/nathaniel/Desktop/Project_aws_boto3/src/Downloads/african_crises.csv')
