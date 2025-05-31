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
