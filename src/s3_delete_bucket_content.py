import boto3
import logging
from botocore.exceptions import ClientError

# Iniatialise a session
session = boto3.Session()

# Initialize logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def delete_bucket_content(bucket_name): 
    try:
        s3_client = session.client('s3')
        # List objects in bucket
        objects = s3_client.list_objects_v2(Bucket=bucket_name).get('Contents',[])

        # Check if there are objects to delete
        if objects:
            # Prepare the list of keys to delete 
            delete_keys = {'Objects': [{'Key': obj['Key']} for obj in objects]}
            response = s3_client.delete_objects(Bucket=bucket_name, Delete=delete_keys)
            deleted = response.get('Deleted', [])

            print(f"Contents in {bucket_name} deleted")
    except ClientError as e:
        logging.error(e)
        return False
    return True     

delete_bucket_content(bucket_name='natebucket007')
        