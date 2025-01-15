import argparse
import pandas as pd
from sqlalchemy import create_engine
from io import BytesIO, TextIOWrapper
import gzip
import requests
# import sys
# sys.executable  这两个是输出这个文件用的python解释器


def main(params):
    user = params.user
    host = params.host
    port = params.port
    db = params.db
    table_name = params.table_name
    url = params.url
    password = params.password
    
    response = requests.get(url)
    

    with gzip.GzipFile(fileobj=BytesIO(response.content)) as gz:
        df_iter = pd.read_csv(TextIOWrapper(gz), iterator=True, chunksize=100000)
    
        df = next(df_iter)
        df.lpep_pickup_datetime = pd.to_datetime(df.lpep_pickup_datetime)
        df.lpep_dropoff_datetime = pd.to_datetime(df.lpep_dropoff_datetime)
        
        engine = create_engine(f'postgresql://{user}:{password}@{host}:{port}/{db}')
        with engine.connect() as conn:
            print("数据库连接成功！")
        

        df.to_sql(name=table_name,con=engine,if_exists='replace')
        while True:
            try:
                # 获取下一批数据
                df = next(df_iter)
                
                # 转换时间格式
                df.lpep_pickup_datetime = pd.to_datetime(df.lpep_pickup_datetime)
                df.lpep_dropoff_datetime = pd.to_datetime(df.lpep_dropoff_datetime)
                
                # 写入数据库
                df.to_sql(name=table_name, con=engine, if_exists='append')
            except StopIteration:
                # 当 df_iter 耗尽时退出循环
                print("All data has been processed.")
                break
    
        
        
if __name__ == '__main__':
    
    parser = argparse.ArgumentParser(description='Ingest CSV data to Postgres')

    parser.add_argument('--user',help='username for postgres')
    parser.add_argument('--pass',help='password for postgres')
    parser.add_argument('--host',help='host for postgres')
    parser.add_argument('--port',help='port for postgres')
    parser.add_argument('--db',help='db for postgres')
    parser.add_argument('--table_name',help='name of the table where we will write the results to')
    parser.add_argument('--url',help='url of the csv file')
    parser.add_argument('--password',help='password for postgres')

    args = parser.parse_args()

    main(args)



  

