import requests

def obtener_precio_bitcoin():
    try:
    
        respuesta = requests.get('https://api.coindesk.com/v1/bpi/currentprice.json')
        respuesta.raise_for_status()  
        datos = respuesta.json()
        precio_usd = datos['bpi']['USD']['rate_float']  
        return precio_usd
    except requests.RequestException:
        print("No se pudo conectar a la API.")
        return None

def calcular_costo_bitcoins():
    n = float(input("Ingrese la cantidad de Bitcoins que posee: "))
    precio_bitcoin = obtener_precio_bitcoin()
    
    if precio_bitcoin is not None:
        costo_total = n * precio_bitcoin
        print(f"El costo actual de {n} Bitcoins es: ${costo_total:,.4f}")
    else:
        print("No se pudo calcular el costo debido a un error en la conexión.")

calcular_costo_bitcoins()
