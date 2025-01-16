import boto3
import logging
import boto3.session
from botocore.exceptions import ClientError

# Initialize session
session = boto3.Session()

# Initialize logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')


# defining a function to listing the buckets in an s3
def list_buckets(region):
    try:
        # initialize the s3 client
        s3_client = session.client('s3')

        #List all buckets
        response = s3_client.list_buckets()
        buckets = response.get('Buckets',[])
        print(f'Buckets available: {buckets}')
    
    except ClientError as e:
        logging.error(e)
        return False
    return True

# Call the function
list_buckets('us-east-1')

