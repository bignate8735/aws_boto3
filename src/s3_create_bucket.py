import boto3
import logging
from botocore.exceptions import ClientError




session = boto3.Session()


# Initialize an S3 client using the session
s3_client = session.client('s3')

bucket_name = 'natebucket007'                  # Replace with your desired unique bucket name
region = 'us-east-1'                           # Specify your preferred region here

                                                    
def create_bucket(bucket_name, region):        # Function to create S3 bucket with error handling
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
create_bucket(bucket_name, region)

# Enable versioning on the bucket
versioning_response = s3_client.put_bucket_versioning(
    Bucket=bucket_name,
    VersioningConfiguration={
        'Status': 'Enabled'  # Enable versioning on the bucket
            }
        )
print(f'Versioning enabled on {bucket_name}')












