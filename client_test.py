# 1. 引用 pymongo 套件
from pymongo import MongoClient

# 2. 建立連線
#    因為 MongoDB 安裝在你的電腦上，所以連線位址是 localhost
#    預設的連接埠 (port) 是 27017
client = MongoClient("mongodb://localhost:27017/")

# 3. 選擇資料庫
#    如果這個資料庫不存在，PyMongo 會在你第一次使用時自動建立
db = client["my_first_database"]

# 4. 選擇集合
#    同樣地，如果這個集合不存在，也會自動建立
collection = db["users"]

# 5. 檢查連線是否成功
#    這行會印出資料庫中的所有集合名稱，如果成功，就代表連線沒問題！
print("成功連線到資料庫！")
print("目前的集合有:", db.list_collection_names())

# 6. 關閉連線 (好習慣)
client.close()
