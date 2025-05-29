from pymongo import MongoClient

# --- 連線到資料庫 ---
client = MongoClient("mongodb://localhost:27017/")
db = client["my_first_database"]
collection = db["users"]

# --- 開始查詢 ---

print("--- 1. 查詢第一筆資料 ---")
# find_one() 不加任何條件，會回傳集合中的任意一筆資料
first_user = collection.find_one()
print(first_user)
print("\n" + "=" * 30 + "\n")  # 分隔線


print("--- 2. 查詢所有資料 ---")
# find() 不加任何條件，會回傳所有資料
# 回傳的是一個游標 (cursor)，我們需要用 for 迴圈把它印出來
all_users = collection.find()
for user in all_users:
    print(user)
print("\n" + "=" * 30 + "\n")


print("--- 3. 條件查詢：找出所有住在'台北'的人 ---")
# 在 find() 中放入一個字典作為查詢條件
query_taipei = {"city": "台北"}
taipei_users = collection.find(query_taipei)
for user in taipei_users:
    print(user)
print("\n" + "=" * 30 + "\n")

print("--- 4. 條件查詢：找出所有 25 歲的人 ---")
# 查詢數字條件
query_age = {"age": 25}
age_25_users = collection.find(query_age)
for user in age_25_users:
    print(user)
print("\n" + "=" * 30 + "\n")

print("--- 5. 正在查詢作者Jason的資料... ---")
# 查詢剛剛插入的資料並印出
query_author = {"作者": "Jason"}
author_jason = collection.find_one(query_author)
print(author_jason)

# --- 關閉連線 ---
client.close()
