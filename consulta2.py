from pymongo import MongoClient

client = MongoClient("mongodb://luis:2002@localhost:27017/admin")
db = client["miBaseDeDatos"]

print("Top 5 jugadores con más partidos ganados en 2022:\n")
resultado = db.datos_excel.aggregate([
    { "$match": { "año": 2022 } },
    { "$group": { "_id": "$Winner", "total_ganados": { "$sum": 1 } } },
    { "$sort": { "total_ganados": -1 } },
    { "$limit": 5 }
])

for doc in resultado:
    print(doc)
