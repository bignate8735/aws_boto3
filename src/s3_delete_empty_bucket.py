import boto3
from botocore.exceptions import ClientError
import logging

# Initialize a session
session = boto3.Session()

# Define a function to delete empty bucket
def delete_empty_bucket(bucket_name):
    try:
        s3_client = session.client('s3')
        # Attempt to delete the bucket
        s3_client.delete_bucket(Bucket = bucket_name)
        print (f"Bucket '{bucket_name}' deleted successfully.")
    except ClientError as e:
        logging.error(e)
        return False
    return True
    print(f"unexpected error: {e}")    


delete_empty_bucket(bucket_name = 'abouttodelete')