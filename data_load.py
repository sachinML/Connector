import boto3
import json
import os
from botocore.exceptions import ClientError
import logging

directory = "C:\\Users\\Visitor\\API\\tmp"
try:
    my_bucket = s3.Bucket('storeapidata')
    my_bucket.objects.all().delete()
    print("Objects from Bucket deleted Successfully.")
except ClientError as e:
    print(logging.error(e))

