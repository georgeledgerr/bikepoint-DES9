import os
import json
import logging
import boto3
from dotenv import load_dotenv

load_dotenv()

load_dotenv()
AWS_ACCESS_KEY = os.getenv('AWS_ACCESS_KEY') #loads in api key
AWS_SECRET_ACCESS_KEY = os.getenv('AWS_SECRET_ACCESS_KEY') #loads in secret key
AWS_BUCKET_NAME= os.getenv('AWS_BUCKET_NAME') #loads in AWS bucket which makes it easier to give this script to someone else

#print(AWS_ACCESS_KEY)
#print(AWS_SECRET_ACCESS_KEY)

data_dir = 'data'
#test_file = '2026-11-11 15-30-11.json'
file_location = os.listdir(data_dir)

s3_client = boto3.client(
    's3',
    aws_access_key_id=AWS_ACCESS_KEY,
    aws_secret_access_key=AWS_SECRET_ACCESS_KEY
)

for file in file_location:
    to_upload = f'{data_dir}/{file}'
    try:
        s3_client.upload_file(to_upload, AWS_BUCKET_NAME, file) #file location, bucket name, file name
        print(f'File {file} successfully uploaded')
        os.remove(to_upload)
    except Exception as e:
        print(f'Something went wrong. Error {e}')