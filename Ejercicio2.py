from pyfiglet import Figlet
import random

def generar_texto_figlet():
    figlet = Figlet()
    fuentes_disponibles = figlet.getFonts()
    
    fuente = input("Ingrese el nombre de la fuente (deje en blanco para aleatoria): ")
    if not fuente:
        fuente = random.choice(fuentes_disponibles)
    
    texto = input("Ingrese el texto a mostrar: ")
    
    try:
        figlet.setFont(font=fuente)
        print(figlet.renderText(texto))
    except Exception as e:
        print(f"Error al establecer la fuente: {e}")

generar_texto_figlet()
