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

- # A table of all s3_client operations and their methods and parameters 

# S3 Operations and Methods

| **Category**        | **Operation**                     | **Method**                              | **Key Parameters**                                                                 |
|----------------------|-----------------------------------|-----------------------------------------|------------------------------------------------------------------------------------|
| **Bucket Operations** | Create a bucket                  | `create_bucket()`                       | `Bucket` (name), `CreateBucketConfiguration` (region constraint)                  |
|                      | Delete a bucket                  | `delete_bucket()`                       | `Bucket` (name)                                                                   |
|                      | List buckets                     | `list_buckets()`                        | None                                                                              |
|                      | Get bucket location              | `get_bucket_location()`                 | `Bucket` (name)                                                                   |
|                      | Get bucket ACL                   | `get_bucket_acl()`                      | `Bucket` (name)                                                                   |
|                      | Put bucket ACL                   | `put_bucket_acl()`                      | `Bucket`, `ACL` (public-read, private, etc.)                                      |
|                      | Get bucket policy                | `get_bucket_policy()`                   | `Bucket`                                                                          |
|                      | Put bucket policy                | `put_bucket_policy()`                   | `Bucket`, `Policy` (JSON string)                                                 |
|                      | Delete bucket policy             | `delete_bucket_policy()`                | `Bucket`                                                                          |
|                      | Get bucket lifecycle config      | `get_bucket_lifecycle_configuration()`  | `Bucket`                                                                          |
|                      | Put bucket lifecycle config      | `put_bucket_lifecycle_configuration()`  | `Bucket`, `LifecycleConfiguration`                                               |
|                      | Delete bucket lifecycle config   | `delete_bucket_lifecycle()`             | `Bucket`                                                                          |
|                      | Enable bucket versioning         | `put_bucket_versioning()`               | `Bucket`, `VersioningConfiguration`                                              |
|                      | Get bucket versioning status     | `get_bucket_versioning()`               | `Bucket`                                                                          |
|                      | Get bucket encryption            | `get_bucket_encryption()`               | `Bucket`                                                                          |
|                      | Put bucket encryption            | `put_bucket_encryption()`               | `Bucket`, `ServerSideEncryptionConfiguration`                                     |
|                      | Delete bucket encryption         | `delete_bucket_encryption()`            | `Bucket`                                                                          |

| **Object Operations** | Upload an object                 | `put_object()`                          | `Bucket`, `Key`, `Body`, `ACL`, `ContentType`, etc.                               |
|                      | Download an object               | `get_object()`                          | `Bucket`, `Key`, `Range`, `ResponseContentType`, etc.                             |
|                      | Delete an object                 | `delete_object()`                       | `Bucket`, `Key`                                                                   |
|                      | Delete multiple objects          | `delete_objects()`                      | `Bucket`, `Delete` (list of `Objects`)                                           |
|                      | Copy an object                   | `copy_object()`                         | `Bucket`, `CopySource`, `Key`, `ACL`, etc.                                        |
|                      | List objects in a bucket         | `list_objects_v2()`                     | `Bucket`, `Prefix`, `MaxKeys`, `ContinuationToken`                                |
|                      | List object versions             | `list_object_versions()`                | `Bucket`, `Prefix`, `KeyMarker`, `VersionIdMarker`, `MaxKeys`                    |
|                      | Get object metadata              | `head_object()`                         | `Bucket`, `Key`                                                                   |
|                      | Get object tagging               | `get_object_tagging()`                  | `Bucket`, `Key`                                                                   |
|                      | Put object tagging               | `put_object_tagging()`                  | `Bucket`, `Key`, `Tagging`                                                       |
|                      | Delete object tagging            | `delete_object_tagging()`               | `Bucket`, `Key`                                                                   |

| **Multipart Uploads** | Initiate multipart upload        | `create_multipart_upload()`             | `Bucket`, `Key`, `ContentType`, etc.                                              |
|                      | Upload a part                    | `upload_part()`                         | `Bucket`, `Key`, `UploadId`, `PartNumber`, `Body`                                 |
|                      | List parts                       | `list_parts()`                          | `Bucket`, `Key`, `UploadId`, `PartNumberMarker`                                   |
|                      | Complete multipart upload        | `complete_multipart_upload()`           | `Bucket`, `Key`, `UploadId`, `MultipartUpload`                                    |
|                      | Abort multipart upload           | `abort_multipart_upload()`              | `Bucket`, `Key`, `UploadId`                                                       |

| **Presigned URL**     | Generate a presigned URL         | `generate_presigned_url()`              | `ClientMethod`, `Params`, `ExpiresIn`, `HttpMethod`                               |
|                      | Generate a presigned POST policy | `generate_presigned_post()`             | `Bucket`, `Key`, `Fields`, `Conditions`, `ExpiresIn`                              |

| **Bucket Analytics**  | Get analytics config            | `get_bucket_analytics_configuration()`  | `Bucket`, `Id`                                                                    |
|                      | Put analytics config             | `put_bucket_analytics_configuration()`  | `Bucket`, `Id`, `AnalyticsConfiguration`                                         |
|                      | Delete analytics config          | `delete_bucket_analytics_configuration()` | `Bucket`, `Id`                                                                   |
|                      | Get metrics config               | `get_bucket_metrics_configuration()`    | `Bucket`, `Id`                                                                    |
|                      | Put metrics config               | `put_bucket_metrics_configuration()`    | `Bucket`, `Id`, `MetricsConfiguration`                                           |
|                      | Delete metrics config            | `delete_bucket_metrics_configuration()` | `Bucket`, `Id`                                                                    |

| **Other Operations**  | Select object content           | `select_object_content()`               | `Bucket`, `Key`, `Expression`, `ExpressionType`, etc.                             |
|                      | Restore archived object          | `restore_object()`                      | `Bucket`, `Key`, `RestoreRequest`                                                |
|                      | Get bucket notification config   | `get_bucket_notification_configuration()` | `Bucket`                                                                         |
|                      | Put bucket notification config   | `put_bucket_notification_configuration()` | `Bucket`, `NotificationConfiguration`                                           |
|                      | Get bucket logging               | `get_bucket_logging()`                  | `Bucket`                                                                          |
|                      | Put bucket logging               | `put_bucket_logging()`                  | `Bucket`, `BucketLoggingStatus`                                                  |
