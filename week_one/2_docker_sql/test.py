import requests
import gzip
from io import BytesIO, TextIOWrapper
import pandas as pd




# response = requests.get('https://github.com/DataTalksClub/nyc-tlc-data/releases/download/yellow/yellow_tripdata_2021-01.csv.gz')

# print(response.status_code)

# with gzip.GzipFile(fileobj=BytesIO(response.content)) as gz:
#     df_iter = pd.read_csv(TextIOWrapper(gz), iterator=True, chunksize=100000)
#     df = next(df_iter)
#     print(type(df))
#     df.tpep_pickup_datetime = pd.to_datetime(df.tpep_pickup_datetime)
#     df.tpep_dropoff_datetime = pd.to_datetime(df.tpep_dropoff_datetime)
#     print(df.head(10))



a = True
if a:
    b = 1
else:
    b=2
print(b)
    
    
    
    
