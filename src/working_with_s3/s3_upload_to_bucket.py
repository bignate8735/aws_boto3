import os
import boto3
import logging
import boto3 
from botocore.exceptions import ClientError


# Initialize a session
session = boto3.Session()

# Initialize logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')


def upload_file(file_path, bucket_name, s3_object_name):   
    try:
        if s3_object_name is None:
            s3_object_name = os.path.basename(file_path)

        s3_client = session.client('s3')
        response = s3_client.upload_file(
            Filename=file_path,       # Local file to upload
            Bucket=bucket_name,       # S3 bucket name
            Key=s3_object_name      # Object name in S3 (path inside the bucket)
            
        )
        print(f"File {file_path} uploaded successfully to {bucket_name}/{s3_object_name}")

    except ClientError as e:
        logging.error(e)
        return False
    return True
    # Handle any errors that occur during upload
    print(f"Error uploading file: {e}")
    
#call the function
upload_file()

  
