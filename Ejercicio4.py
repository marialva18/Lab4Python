def procesar_temperaturas():
    try:
        with open('temperaturas.txt', 'r') as archivo:
            temperaturas = [linea.strip().split(',') for linea in archivo]
        
        total_temperaturas = sum(float(temp[1]) for temp in temperaturas)
        temperatura_promedio = total_temperaturas / len(temperaturas)
        temperatura_maxima = max(float(temp[1]) for temp in temperaturas)
        temperatura_minima = min(float(temp[1]) for temp in temperaturas)

        with open('resumen_temperaturas.txt', 'w') as resumen:
            resumen.write(f"Temperatura Promedio: {temperatura_promedio:.2f}°C\n")
            resumen.write(f"Temperatura Máxima: {temperatura_maxima:.2f}°C\n")
            resumen.write(f"Temperatura Mínima: {temperatura_minima:.2f}°C\n")
        
        print("Resumen de temperaturas generado exitosamente.")
    except FileNotFoundError:
        print("El archivo 'temperaturas.txt' no existe.")
    except Exception as e:
        print(f"Error al procesar las temperaturas: {e}")

procesar_temperaturas()
