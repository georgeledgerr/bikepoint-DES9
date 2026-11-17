from datetime import datetime
from modules.extract_function import extract_to_json
import logging
import os

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

url='https://api.tfl.gov.uk/BikePoint/'
data_dir = 'data'

extract_result = extract_to_json(url,data_dir,timestamp,max_attempts=3)

print(extract_result)
