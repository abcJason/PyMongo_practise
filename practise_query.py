from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")
db = client["my_first_database"]
collection = db["users"]
print(f"成功連線! 目前的集合有: {db.list_collection_names()}")

client.close()
