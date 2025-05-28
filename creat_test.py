from pymongo import MongoClient

# --- 連線到資料庫 ---
client = MongoClient("mongodb://localhost:27017/")
db = client["my_first_database"]
collection = db["users"]

# --- 準備要新增的資料 ---
# 資料是用 Python 字典的格式來表示
# 我們準備了三位使用者的資料
users_data = [
    {"name": "小明", "age": 25, "city": "台北"},
    {"name": "小華", "age": 30, "city": "新竹"},
    {"name": "小英", "age": 25, "city": "台北"},
]

# --- 新增資料到集合中 ---
# 使用 insert_many() 可以一次新增多筆資料
# 為了避免重複新增，我們先清空集合 (測試時常用)
collection.delete_many({})
result = collection.insert_many(users_data)

# --- 顯示新增結果 ---
print(f"成功新增了 {len(result.inserted_ids)} 筆資料。")

# --- 關閉連線 ---
client.close()
