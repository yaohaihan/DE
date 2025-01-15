import pandas as pd
from sqlalchemy import create_engine


df = pd.read_csv('taxi_zone_lookup.csv')

print(df.head())

engine = create_engine('postgresql://postgres:hhelibeblxyhh123@35.186.145.26:5432/ny_taxi')
engine.connect()

df.to_sql(name='zones',con=engine,if_exists='replace')


