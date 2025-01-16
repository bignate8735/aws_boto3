import boto3
import logging
from botocore.exceptions import ClientError

# Initialize session
session = boto3.Session()

# Initialize logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')


def create_bucket(bucket_name, region):                         # Function to create S3 bucket with error handling
    try:
        if region == 'us-east-1':
            s3_client = session.client('s3')
            s3_client.create_bucket(Bucket = bucket_name, ACL ='private')
        else:
            s3_client = session.client('s3',region_name=region)

            s3_client.create_bucket(
            Bucket=bucket_name,                                 # Name of the bucket to be created
            CreateBucketConfiguration = {
                'LocationConstrainst': region                   # Location configuration for non-us-east-1 regions
            },  
            ACL = 'private'                                                                                                  #   Specifies the region for the bucket (mandatory for all regions except 'us-east-1')
            )        
        print(f'Bucket {bucket_name} created successfully in {region}')

    except ClientError as e:
        logging.error(e)
        return False
    return True 
        

# Call the function to create the bucket and enable versioning
create_bucket(bucket_name='abouttodelete', region= 'us-east-1')
bucket_name='abouttodelete'
# Enable versioning on the bucket
s3_client =session.client('s3')
versioning_response = s3_client.put_bucket_versioning(
    Bucket= bucket_name,
    VersioningConfiguration={
        'Status': 'Enabled'  # Enable versioning on the bucket
    }
)
print(f'Versioning enabled on bucket')












