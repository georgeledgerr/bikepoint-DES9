import os
import requests
import json
from datetime import datetime
import time
import logging


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

data_dir = 'data' #naming folder where data is stored
os.makedirs(data_dir, exist_ok=True) #makes the file and exist_ok means that if it exists already then its okay
filename = f'{data_dir}/{timestamp}.json' #filepath i.e. goto the directory for this repo and save this file i.e. data/...

url='https://api.tfl.gov.uk/BikePoint/'

#print(filename)

attempt = 1
max_attempts = 3

while attempt <= max_attempts:
    response = requests.get(url)
    status_code = response.status_code

    if 200<=status_code<300:
        try:
            data = response.json()

            with open(filename,'w') as file:
                json.dump(data, file)
            print(f'File {filename} saved successfully 😁')
            logger.info(f'File {filename} saved successfully 😁')
        except Exception as e:
            print(f'An error occured when saving the JSON: {e}')
            logger.error(f'An error occured when saving the JSON: {e}')
    
        break

    elif 300<= status_code <500:
        print(f'API call fail, here is the status code {status_code}')
        logger.error(f'API call fail, here is the status code {status_code}')
        break

    else:
        if attempt == max_attempts:
            print(f'Max attempts reached. Status code {status_code}. Investigate further.')
            logger.warning(f'Max attempts reached. Status code {status_code}. Investigate further.')
        else:
            print(f'Attempt {attempt} failed, status code {status_code}. Lets go again D:')
            logger.error(f'Attempt {attempt} failed, status code {status_code}. Lets go again D:')

        attempt+=1
        time.sleep(30)