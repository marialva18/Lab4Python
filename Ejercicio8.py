import csv
import sqlite3

def obtener_tipo_cambio(fecha):
    
    conexion = sqlite3.connect('base.db')
    cursor = conexion.cursor()

    
    cursor.execute('SELECT venta FROM sunat_info WHERE fecha = ?', (fecha,))
    resultado = cursor.fetchone()

    
    conexion.close()

    if resultado:
       
        return resultado[0]
    else:
        print(f"No se encontró el tipo de cambio para la fecha {fecha}.")
        return None

def procesar_ventas():
    try:
        
        with open('ventas.csv', 'r') as archivo_csv:
            lector_csv = csv.reader(archivo_csv)
            encabezado = next(lector_csv)  

            print("Producto, Fecha, Precio en Dólares, Precio en Soles")
            for fila in lector_csv:
                producto, fecha, precio_dolares = fila[0], fila[1], float(fila[2])

               
                tipo_cambio_venta = obtener_tipo_cambio(fecha)

                if tipo_cambio_venta is not None:
                   
                    precio_soles = precio_dolares * tipo_cambio_venta
                   
                    print(f"{producto}, {fecha}, ${precio_dolares:.2f}, S/.{precio_soles:.2f}")
                else:
                    print(f"No se pudo calcular el precio en soles para el producto {producto} en la fecha {fecha}.")

    except FileNotFoundError:
        print("El archivo 'ventas.csv' no existe.")
    except Exception as e:
        print(f"Ocurrió un error: {e}")


procesar_ventas()
