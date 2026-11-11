import os
import requests
import json
from datetime import datetime
import time

timestamp = datetime.now().strftime('%Y-%m-%d %H-%M-%S') #timestamp for our data and filename
#print(timestamp)
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

    if 200<=status_code<300
        data = response.json()

        with open(filename,'w') as file:
            json.dump(data, file)

        print(f'File {filename} saved successfully 😁')
        break

    elif 300<= status_code <500:
        print(f'API call fail, here is the status code {status_code}')
        break

    else:
        if attempt == max_attempts:
            print(f'Max attempts reached. Status code {status_code}. Investigate further.')
        else:
            print(f'Attempt {attempt} failed, status code {status_code}. Lets go again D:')

        attempt+=1
        time.sleep(30)