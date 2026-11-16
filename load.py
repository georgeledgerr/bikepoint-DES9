# --- Imports -----------------------------------------------------------------
import os                       # read .env values, list and delete files
import json
import logging
import boto3                    # AWS's Python package: talks to S3
from dotenv import load_dotenv  # reads the .env file


# --- Credentials (from .env) -------------------------------------------------
load_dotenv()                   # read .env into the environment

load_dotenv()
AWS_ACCESS_KEY = os.getenv('AWS_ACCESS_KEY') #loads in api key
AWS_SECRET_ACCESS_KEY = os.getenv('AWS_SECRET_ACCESS_KEY') #loads in secret key
AWS_BUCKET_NAME= os.getenv('AWS_BUCKET_NAME') #loads in AWS bucket which makes it easier to give this script to someone else

#print(AWS_ACCESS_KEY)
#print(AWS_SECRET_ACCESS_KEY)


# --- Files to upload ---------------------------------------------------------
data_dir = 'data'               # folder extract.py saves into
#test_file = '2026-11-11 15-30-11.json'
file_location = os.listdir(data_dir)   # list of every file name in data/


# --- Connect to S3 -----------------------------------------------------------
# A client is the connection to an AWS service. Here: S3, using our keys.
s3_client = boto3.client(
    's3',
    aws_access_key_id=AWS_ACCESS_KEY,
    aws_secret_access_key=AWS_SECRET_ACCESS_KEY
)


# --- Upload each file, then delete the local copy ----------------------------
for file in file_location:
    to_upload = f'{data_dir}/{file}'   # full path, e.g. data/2026-11-16 13-00-00.json
    try:
        s3_client.upload_file(to_upload, AWS_BUCKET_NAME, file) #file location, bucket name, file name
        print(f'File {file} successfully uploaded')
        os.remove(to_upload)           # only reached if the upload worked, so nothing is lost
    except Exception as e:
        # Upload failed (e.g. wrong keys, no internet, bucket not found):
        # the file stays in data/ so the next run can try again
        print(f'Something went wrong. Error {e}')