import pandas as pd
from pymongo import MongoClient

client = MongoClient('mongodb://localhost:27017')
db = client['StockData']
collection = db['News']

chunk_size = 10000  
for chunk in pd.read_csv('../nasdaq_exteral_data.csv', chunksize=chunk_size):
    data = chunk.to_dict(orient='records')
    collection.insert_many(data)


client.close()