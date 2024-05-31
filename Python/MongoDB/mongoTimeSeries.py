import json
from datetime import datetime
import uuid
import pymongo

name = "indlejrede_test"
host = "mongodb://localhost:27017/"
device_id_0 = uuid.uuid4()

conn = pymongo.MongoClient(host)
#conn.test.create_collection("temperature", timeseries={"timeField": "timestamp"})
#db.command('create', 'testCollection', timeseries={ 'timeField': 'timestamp', 'metaField': 'data', 'granularity': 'hours' })


'''
Time series database will automatically insert the timestamp field if it is not present in the data.
'''
def insertdata(db: pymongo.database.Database, collection: str, data: dict) -> None:
    col = db[collection]
    col.insert_one(data)

