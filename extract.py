import os
import requests
import json
from datetime import datetime

timestamp = datetime.now().strftime('%Y-%m-%d %H-%M-%S') #timestamp for our data and filename
#print(timestamp)
data_dir = 'data' #naming folder where data is stored
os.makedirs(data_dir, exist_ok=True) #makes the file and exist_ok means that if it exists already then its okay
filename = f'{data_dir}/{timestamp}.json' #filename will be data/timestamp

url='https://api.tfl.gov.uk/BikePoint/'

#print(filename)

response = requests.get(url)

data = response.json()

#print(data)

with open(filename,'w') as file:
    json.dump(data, file)