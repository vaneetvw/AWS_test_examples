# Mathis Van Eetvelde 1st March 2018
# Automatic directory upload to AWS s3 bucket
# Where to get access key: https://aws.amazon.com/blogs/security/wheres-my-secret-access-key/


import boto3
import os
from botocore.client import Config


#CREDENTIALS
ACCESS_KEY_ID = "public access key"
ACCESS_SECRET_KEY = "secret access key"
BUCKET_NAME = "bucket name"

#FILE AND DIR SPECIFICATION
FILE_NAME=""
DIR_NAME="dir you want to upload to specified bucket ea: C:/Documents/folder"
iteration = 0

#Connect to s3
s3 = boto3.resource(
    "s3",
    aws_access_key_id=ACCESS_KEY_ID,
    aws_secret_access_key=ACCESS_SECRET_KEY,
    config=Config(signature_version="s3v4")
)

#Cycle trough dir and upload to s3 bucket
for filename in os.listdir(DIR_NAME):
    print(filename)
    FILE_NAME = (DIR_NAME + '/' + filename)
    print(FILE_NAME)
    data = open(FILE_NAME, "rb")
    s3.Bucket(BUCKET_NAME).put_object(Key=filename, Body=data)
    FILE_NAME = ""

#listing files in s3 bucket
listObjSummary = s3.Bucket(BUCKET_NAME).objects.all()

for objSum in listObjSummary:
    iteration += 1
    print("Item {}: {}".format(iteration, objSum.key))