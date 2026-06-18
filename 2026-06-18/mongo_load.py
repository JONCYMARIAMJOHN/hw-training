import pandas as pd
from pymongo import MongoClient

df = pd.read_csv("/home/user/Downloads/2026-06-18/DataHut_CH_Denner_FullDump_20260618.CSV", sep="|")

client = MongoClient("mongodb://localhost:27017/")
db = client["FirstDB"]

db.denner.insert_many(df.to_dict("records"))