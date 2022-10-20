import boto3
import json
import os
from botocore.exceptions import ClientError
import logging

directory = "C:\\Users\\Visitor\\API\\tmp"

# delete content from the bucket(if any exist in prior)
try:
    my_bucket = s3.Bucket('storeapidata')
    my_bucket.objects.all().delete()
    print("Objects from Bucket deleted Successfully.")
except ClientError as e:
    print(logging.error(e))
    
# delete bucket itself    
try:
    response = client.delete_bucket(Bucket='storeapidata')
    print("Bucket Deleted Successfully")
    print(json.dumps(response, indent=2))
except ClientError as e:
    print(logging.error(e))
    
# bucket creation    
response = client.create_bucket(
    ACL='private',
    Bucket='storeapidata',
    CreateBucketConfiguration={
        'LocationConstraint': 'us-west-2',
    },
)

print("New bucket has been created.")
print(json.dumps(response, indent=2))
# upload file in the the bucket
for file in os.listdir(directory):
    client.upload_file(directory+'\\' + file, 'storeapidata', file)
