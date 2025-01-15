import requests
import pandas as pd

url = 'https://github.com/DataTalksClub/nyc-tlc-data/releases/download/yellow/yellow_tripdata_2021-01.csv.gz'

response = requests.get(url)
print(type(response.content))