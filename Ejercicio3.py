import requests
import zipfile
import os

def descargar_imagen():
    url = "https://images.unsplash.com/photo-1546527868-ccb7ee7dfa6a?q=80&w=2070&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D"
    nombre_imagen = "imagen_descargada.jpg"
    
    try:
        respuesta = requests.get(url)
        respuesta.raise_for_status()
        with open(nombre_imagen, "wb") as archivo:
            archivo.write(respuesta.content)
        print(f"Imagen descargada exitosamente: {nombre_imagen}")
        return nombre_imagen
    except requests.RequestException:
        print("Error al descargar la imagen.")
        return None

def comprimir_imagen(nombre_imagen):
    nombre_zip = "imagen_comprimida.zip"
    try:
        with zipfile.ZipFile(nombre_zip, 'w') as archivo_zip:
            archivo_zip.write(nombre_imagen)
        print(f"Imagen comprimida en: {nombre_zip}")
    except Exception as e:
        print(f"Error al comprimir la imagen: {e}")

def descomprimir_imagen(nombre_zip):
    try:
        with zipfile.ZipFile(nombre_zip, 'r') as archivo_zip:
            archivo_zip.extractall("descomprimido")
        print("Imagen descomprimida en la carpeta 'descomprimido'.")
    except Exception as e:
        print(f"Error al descomprimir la imagen: {e}")

nombre_imagen = descargar_imagen()
if nombre_imagen:
    comprimir_imagen(nombre_imagen)
    descomprimir_imagen("imagen_comprimida.zip")
    os.remove(nombre_imagen)  # Eliminar la imagen descargada original para limpieza
