from pymongo import MongoClient
import datetime

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

# 準備一筆要插入的資料
post = {
    "作者": "Jason",
    "內容": "我的第一篇部落格文章與 Docker MongoDB 相關！",
    "標籤": ["mongodb", "python", "docker"],
    "日期": datetime.datetime.now(datetime.timezone.utc),
}

# --- 新增資料到集合中 ---
# 使用 insert_many() 可以一次新增多筆資料
# 為了避免重複新增，我們先清空集合 (測試時常用)
collection.delete_many({})
result = collection.insert_many(users_data)
# --- 顯示新增結果 ---
print(f"成功新增了 {len(result.inserted_ids)} 筆資料。")

# 插入資料
post_id = collection.insert_one(post).inserted_id
print(f"資料已成功插入，ID 為：{post_id}")


# --- 關閉連線 ---
client.close()
