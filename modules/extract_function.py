import os
import requests
import json
from datetime import datetime
import time
import logging

logger = logging.getLogger(__name__)

def extract_to_json(url:str, data_dir:str, timestamp:str, max_attempts:int):
    """Function to extract JSON from a URL and save to a destination

    Args:
        url (str): URL to pull data from
        data_dir (str): filepath to save data
        timestamp (str): timestamp to attend to file name
        max_attempts (int): max number of retries when calling to API
    """

    #make directory if doesnt exist
    os.makedirs(data_dir, exist_ok=True)

    #build out the file name
    filename = f'{data_dir}/{timestamp}.json'

    attempt = 1

    while attempt <= max_attempts:
        response = requests.get(url)
        status_code = response.status_code

        if 200 <= status_code < 300:
            try:
                data = response.json()

                with open(filename, 'w') as file:
                    json.dump(data, file)
                print(f'File {filename} saved successfully 😁')
                logger.info(f'File {filename} saved successfully 😁')

                #Flag that data was saved successfully
                return True
            
            except Exception as e:
                print(f'An error occured when saving the JSON: {e}')
                logger.error(f'An error occured when saving the JSON: {e}')
            break

        elif 300 <= status_code < 500:
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

            attempt += 1
            time.sleep(30)

    # return statement
    return False