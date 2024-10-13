def generar_tabla(n):
    nombre_archivo = f"tabla-{n}.txt"
    with open(nombre_archivo, 'w') as archivo:
        for i in range(1, 11):
            archivo.write(f"{n} x {i} = {n * i}\n")
    print(f"Tabla de multiplicar del {n} generada en '{nombre_archivo}'.")

def leer_tabla(n):
    nombre_archivo = f"tabla-{n}.txt"
    try:
        with open(nombre_archivo, 'r') as archivo:
            print(archivo.read())
    except FileNotFoundError:
        print(f"El archivo '{nombre_archivo}' no existe.")

def leer_linea_tabla(n, m):
    nombre_archivo = f"tabla-{n}.txt"
    try:
        with open(nombre_archivo, 'r') as archivo:
            lineas = archivo.readlines()
            if 1 <= m <= len(lineas):
                print(lineas[m - 1].strip())
            else:
                print("El número de línea es inválido.")
    except FileNotFoundError:
        print(f"El archivo '{nombre_archivo}' no existe.")


n = int(input("Ingrese un número para la tabla de multiplicar (1-10): "))
generar_tabla(n)

opcion = input("Desea leer el archivo completo (s/n)? ").lower()
if opcion == 's':
    leer_tabla(n)

m = int(input("Ingrese el número de línea a leer (1-10): "))
leer_linea_tabla(n, m)
