import json
from datetime import datetime
import uuid
import pymongo

name = "indlejrede_test"
host = "mongodb://localhost:27017/"
device_id_0 = uuid.uuid4()

def createdb(dbname: str, dbhost: str) -> pymongo.database.Database:
    client = pymongo.MongoClient(dbhost)
    dblist = client.list_database_names()
    if "mydatabase" in dblist:
        print("The database exists.")
    elif "mydatabase" not in dblist:
        mydb = client[dbname]
        return mydb

def insertdata(db: pymongo.database.Database, collection: str, data: dict) -> None:
    col = db[collection]
    col.insert_one(data)

def finddata(db: pymongo.database.Database, collection: str, data: dict) -> list:
    col = db[collection]
    return col.find(data)

def meanAggregate(db: pymongo.database.Database, collection: str, field: str) -> float:
    col = db[collection]
    return col.aggregate([{"$group": {"_id": None, "avg": {"$avg": "$" + field}}}])

def findMinimum(db: pymongo.database.Database, collection: str, field: str) -> float:
    col = db[collection]
    return col.aggregate([{"$group": {"_id": None, "min": {"$min": "$" + field}}}])

def findMaximum(db: pymongo.database.Database, collection: str, field: str) -> float:
    col = db[collection]
    return col.aggregate([{"$group": {"_id": None, "max": {"$max": "$" + field}}}])

def findCount(db: pymongo.database.Database, collection: str, field: str) -> int:
    col = db[collection]
    return col.aggregate([{"$group": {"_id": None, "count": {"$sum": 1}}}])

def deleteCollection(db: pymongo.database.Database, collection: str) -> None:
    col = db[collection]
    col.drop()

def deleteDatabase(db: pymongo.database.Database, dbname: str) -> None:
    db.dropDatabase()

def deleteDocument(db: pymongo.database.Database, collection: str, data: dict) -> None:
    col = db[collection]
    col.delete_one(data)

def updateDocument(db: pymongo.database.Database, collection: str, data: dict, new_data: dict) -> None:
    col = db[collection]
    col.update_one(data, {"$set": new_data})

db = createdb(name, host)
print(db.name + " exists.")

sensor_data = {
    "device": {"device_id": str(device_id_0)}, # UUID4 string
    "temperature": 23.2,
    "humidity": 55,
    "pressure": 1011.4,
    "timestamp": datetime.now().isoformat() # ISO date
}

insertdata(db, "sensor_readings", sensor_data)
print("Data inserted.")

# Filter by device_id
for item in finddata(db, "sensor_readings", {"device.device_id": str(device_id_0)}):
    print(item)

for item in finddata(db, "sensor_readings", {}):
    print(item)

# Search by temperature
#for item in finddata(db, "sensor_readings", {"temp": 20.2}):
#    print(item)

#minimum_temp = findMinimum(db, "sensor_readings", "temperature")
#average_temp = meanAggregate(db, "sensor_readings", "temperature")
#count = findCount(db, "sensor_readings", "temp")

#print(next(iter(average_temp)) if average_temp else {})
#print(next(iter(minimum_temp)) if minimum_temp else {})
#print(next(iter(count)) if count else {})

