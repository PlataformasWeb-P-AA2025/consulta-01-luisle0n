from pymongo import MongoClient

client = MongoClient("mongodb://luis:2002@localhost:27017/admin")
db = client["miBaseDeDatos"]

print("Top 10 jugadores con mayor promedio de sets ganados en 2023:\n")
resultado = db.datos_excel.aggregate([
    { "$match": { "año": 2023 } },
    { "$group": { "_id": "$Winner", "promedio_sets_ganados": { "$avg": "$Wsets" } } },
    { "$sort": { "promedio_sets_ganados": -1 } },
    { "$limit": 10 }
])

for doc in resultado:
    print(doc)
