import requests
import sqlite3
from pymongo import MongoClient

def obtener_tipo_cambio():
    url = "https://api.apis.net.pe/v1/tipo-cambio-sunat"
    try:
        respuesta = requests.get(url)
        respuesta.raise_for_status()
        datos = respuesta.json()
        return datos
    except requests.RequestException:
        print("No se pudo conectar a la API.")
        return None

def almacenar_en_sqlite(datos):
    conexion = sqlite3.connect('base.db')
    cursor = conexion.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS sunat_info (
            fecha TEXT PRIMARY KEY,
            compra REAL,
            venta REAL
        )
    ''')
    for registro in datos:
        cursor.execute('''
            INSERT OR REPLACE INTO sunat_info (fecha, compra, venta) VALUES (?, ?, ?)
        ''', (registro['fecha'], registro['compra'], registro['venta']))
    conexion.commit()
    conexion.close()
    print("Datos almacenados en SQLite con éxito.")

def almacenar_en_mongodb(datos):
    cliente = MongoClient('mongodb://localhost:27017/')
    base_datos = cliente['base_datos_sunat']
    coleccion = base_datos['sunat_info']
    for registro in datos:
        coleccion.update_one(
            {'fecha': registro['fecha']},
            {'$set': {'compra': registro['compra'], 'venta': registro['venta']}},
            upsert=True
        )
    print("Datos almacenados en MongoDB con éxito.")

def mostrar_datos_sqlite():
    conexion = sqlite3.connect('base.db')
    cursor = conexion.cursor()
    cursor.execute('SELECT * FROM sunat_info')
    registros = cursor.fetchall()
    print("Contenido de la tabla sunat_info:")
    for registro in registros:
        print(f"Fecha: {registro[0]}, Compra: {registro[1]:.4f}, Venta: {registro[2]:.4f}")
    conexion.close()

datos_tipo_cambio = obtener_tipo_cambio()

if datos_tipo_cambio:
    almacenar_en_sqlite(datos_tipo_cambio)
    almacenar_en_mongodb(datos_tipo_cambio)
    mostrar_datos_sqlite()
