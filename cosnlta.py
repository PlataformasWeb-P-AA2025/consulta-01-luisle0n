import pandas as pd
from pymongo import MongoClient

# Conexión a MongoDB
client = MongoClient("mongodb://luis:2002@localhost:27017/admin")

db = client["miBaseDeDatos"]
coleccion = db["datos_excel"]

# Leer archivos Excel
archivo_2022 = pd.read_excel("./data/2022.xlsx")
archivo_2023 = pd.read_excel("./data/2023.xlsx")

# Agregar campo "año"
archivo_2022["año"] = 2022
archivo_2023["año"] = 2023

# Convertir a diccionario
datos_2022 = archivo_2022.to_dict(orient="records")
datos_2023 = archivo_2023.to_dict(orient="records")

# Insertar datos
coleccion.insert_many(datos_2022)
coleccion.insert_many(datos_2023)

print("Datos insertados correctamente.\n")

# Consulta 1: Top 5 ganadores 2022
print("Top 5 ganadores 2022:")
pipeline_2022 = [
    { "$match": { "año": 2022 } },
    { "$group": { "_id": "$Winner", "total_ganados": { "$sum": 1 } } },
    { "$sort": { "total_ganados": -1 } },
    { "$limit": 5 }
]
for doc in coleccion.aggregate(pipeline_2022):
    print(doc)

print("\nTop 5 promedio sets ganados 2023:")
# Consulta 2: Top 5 promedio sets ganados 2023
pipeline_2023 = [
    { "$match": { "año": 2023 } },
    { "$group": { "_id": "$Winner", "promedio_sets_ganados": { "$avg": "$Wsets" } } },
    { "$sort": { "promedio_sets_ganados": -1 } },
    { "$limit": 5 }
]
for doc in coleccion.aggregate(pipeline_2023):
    print(doc)
