# This project will teach the fundamentals of working with aws services using the aws CLI and python

## Create and Activate Virtual Environment
- python -m venv venv
- source venv/bin/activate

#### Install boto3
- pip install boto3

#### Install boto3 with crt 

Note: In addition to boto3 default install, we can choose to incliude the new AWS common
Runtime (CRT). the crt is a collection of modular packages that serve as a new foundation
for AWS SDK'S. USING THE CRT, SDK"S can share the same base code when possible, improving
consistency throughput optimization across AWS SDK'S

#### To use the CRT + Boto3, install boto3 like below:
- pip install boto3[crt]

#### To revert to thr thr non crt version of boto3
- pip uninstall awscrt

#### To enable CRT again
- pip install boto3[crt]

#### Save dependencies in requirements.txt
- pip freeze > requirements.txt         

#### Save depencies in requirements.txt
- pip install -r requirements.txt

#### Setting up boto3 to accesss AWS resources/ services
- install CLI from here https://aws.amzon.com/cli
- After create IAM crednetials and run:
- aws configure

#### Passing credentials as parameters
- There are two ways to pass credentials dynamically in the code as credentials 
- 1. while creating boto3 client(client() method)
- 2. while creating boto3 session () method)
exampel:

1. client = boto3.client(
"s3"
aws_acess_key_id = ACCESS_KEY,
aws_secret_key_id = SECRET_KEY,
aws_session_token = SESSION_TOKEN
)

2.  session = boto3.Session(
aws_acess_key_id = ACCESS_KEY,
aws_secret_key_id = SECRET_KEY,
aws_session_token = SESSION_TOKEN
)
Note: Session_Token is needed when using temporary credentials


| Feature              | **Session** (e.g., `boto3.Session()`)                             | **Client** (e.g., `boto3.client()`)                            | **Resource** (e.g., `boto3.resource()`)                    |
|----------------------|-------------------------------------------------------------------|---------------------------------------------------------------|------------------------------------------------------------|
| **Abstraction Level** | High-level, manages configuration and credentials.                | Low-level, closer to raw API calls.                          | High-level, object-oriented abstraction over AWS services. |
| **Ease of Use**       | Used to configure AWS SDK settings (e.g., region, credentials).   | More verbose; requires more boilerplate code.                | Easier and more Pythonic; works like normal Python objects. |
| **Operations**        | Provides context and configuration for creating clients/resources.| Provides direct access to AWS service operations (API calls).| Simplifies working with resources like EC2 instances, S3 buckets, etc. |
| **Customization**     | Controls the region, profile, and credentials for AWS interactions. | Full control, allows fine-grained configuration.             | Less control, but much simpler for common tasks.            |
| **Examples**          | Managing session configurations like AWS credentials and region.| Starting EC2 instances, managing IAM roles.                 | Managing S3 buckets, EC2 instance state, DynamoDB tables.   |

# Note that by default if a session is not created and a client or resource object is created automatically a session is created.

- # s3 bucket creation parameters table

| **Parameter**               | **Description**                                                      |
|-----------------------------|----------------------------------------------------------------------|
| `Bucket`                    | The name of the bucket (required).                                   |
| `CreateBucketConfiguration` | Specify the region for the bucket (optional, if different from default). |
| `ACL`                        | Access control list, e.g., `private`, `public-read`, etc. (optional). |
| `GrantFullControl`           | Grants full control to the specified AWS account (optional).         |
| `VersioningConfiguration`   | Enable or disable versioning for the bucket (optional).             |
| `Tagging`                    | Tags to apply to the bucket (optional).                              |
| `ObjectLockEnabledForBucket`| Enable object lock (optional).                                       |


- # s3 file upload table parameters 
| **Parameter**              | **Description**                                                                 |
|----------------------------|---------------------------------------------------------------------------------|
| `Filename`                 | The local path to the file you want to upload (e.g., `'path/to/your/file.txt'`).|
| `Bucket`                   | The name of the S3 bucket where the file will be uploaded.                     |
| `Key`                      | The name (or path) of the file in the S3 bucket. For example: `'folder/filename.txt'`.|
| `ExtraArgs`                | Optional dictionary for additional arguments (e.g., `ACL`, `Metadata`).        |
| `ACL`                      | Optional: The access control list (ACL) for the file. Defaults to `private`. Other options include `public-read`, `authenticated-read`, etc.|
| `Metadata`                 | Optional: Custom metadata that will be associated with the uploaded object.    |
