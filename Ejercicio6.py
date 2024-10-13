def contar_lineas_codigo(ruta_archivo):
    if not ruta_archivo.endswith('.py'):
        print("El archivo no es un archivo .py válido.")
        return
    
    try:
        with open(ruta_archivo, 'r') as archivo:
            lineas = archivo.readlines()
        
        lineas_codigo = [
            linea for linea in lineas 
            if linea.strip() and not linea.strip().startswith('#')
        ]
        
        numero_lineas = len(lineas_codigo)
        print(f"El archivo '{ruta_archivo}' tiene {numero_lineas} líneas de código.")
    
    except FileNotFoundError:
        print("El archivo especificado no existe.")
    except Exception as e:
        print(f"Ocurrió un error inesperado: {e}")

ruta_archivo = input("Ingrese la ruta del archivo .py: ")
contar_lineas_codigo(ruta_archivo)
