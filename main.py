from datetime import datetime
from modules.extract_function import extract_to_json
import logging
import os
from dotenv import load_dotenv
import boto3
from modules.load_function import load_to_aws

timestamp = datetime.now().strftime('%Y-%m-%d %H-%M-%S') #timestamp for our data and filename
#print(timestamp)

log_dir = 'logs'
os.makedirs(log_dir, exist_ok=True)
log_filename = f'{log_dir}/{timestamp}.log'

logging.basicConfig(
    filename=log_filename,
    format='%(asctime)s - %(levelname)s - %(message)s', 
    level=logging.INFO
)

logger = logging.getLogger()
logger.info('Logger was successfully initialised.')

load_dotenv()
AWS_ACCESS_KEY = os.getenv('AWS_ACCESS_KEY') #loads in api key
AWS_SECRET_ACCESS_KEY = os.getenv('AWS_SECRET_ACCESS_KEY') #loads in secret key
AWS_BUCKET_NAME= os.getenv('AWS_BUCKET_NAME') #loads in AWS bucket which makes it easier to give this script to someone else

s3_client = boto3.client(
    's3',
    aws_access_key_id=AWS_ACCESS_KEY,
    aws_secret_access_key=AWS_SECRET_ACCESS_KEY
)

url='https://api.tfl.gov.uk/BikePoint/'
data_dir = 'data'

extract_result = extract_to_json(url,data_dir,timestamp,max_attempts=3)

print(extract_result)

load_result = load_to_aws(data_dir,AWS_ACCESS_KEY,AWS_SECRET_ACCESS_KEY,AWS_BUCKET_NAME)
