import boto3
import os
from botocore.client import Config


ACCESS_KEY_ID = "-public access key-"
ACCESS_SECRET_KEY = "-secret access key-"
BUCKET_NAME = "-bucket name-"
FILE_NAME=""
DIR_NAME="-dir you want to upload to specified bucket-"
iteration = 0

s3 = boto3.resource(
    "s3",
    aws_access_key_id=ACCESS_KEY_ID,
    aws_secret_access_key=ACCESS_SECRET_KEY,
    config=Config(signature_version="s3v4")
)

for filename in os.listdir(DIR_NAME):
    print(filename)
    FILE_NAME = (DIR_NAME + '/' + filename)
    print(FILE_NAME)
    data = open(FILE_NAME, "rb")
    s3.Bucket(BUCKET_NAME).put_object(Key=filename, Body=data)
    FILE_NAME = ""

listObjSummary = s3.Bucket(BUCKET_NAME).objects.all()

for objSum in listObjSummary:
    iteration += 1
    print("Item {}: {}".format(iteration, objSum.key))