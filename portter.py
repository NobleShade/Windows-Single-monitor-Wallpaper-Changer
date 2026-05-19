#PSEUDOCODIGO

#INICIO
# OBJETIVO: Crear un programa capaz de conectarse a un webserver a través de muchos puertos, hasta encontrar el correcto que permita la conexión. 
#
# 1. Se conecta al puerto del webserver
# 2. Hace una operación en un número
# 3. Pasa a conectarse al siguiente puerto
# Inicia el numero en 0, la pagina te dice el puerto. Una vez conectado, te dice que operación hacer, y el puerto siguiente al que conectarte, ese puerto te dice que operación hacer, y así sucesivamente hasta que la página te diga STOP.
#FIN 

import time 
import requests

host = "x.x.x.x"  # Reemplaza con la dirección IP del servidor 


def consulta_puerto(puerto):
    try:
        response = requests.get(f"http://{host}:{puerto}", timeout=3)
        return response.text
    except requests.exceptions.RequestException as e:
        return None

def parsear_respuesta(respuesta):
    partes = respuesta.split()
    operacion = partes[0]
    if "STOP" in operacion:
        return None
    numero = float(partes[1])
    siguiente_puerto = int(partes[2])
    if siguiente_puerto == 9765:
        return None
    return operacion, numero, siguiente_puerto
    
def realizar_operacion(numero_actual, operacion, numero):
    if operacion == "add":
        return numero_actual + numero
    elif operacion == "minus":
        return numero_actual - numero
    elif operacion == "multiply":
        return numero_actual * numero   
    elif operacion == "divide":
        return numero_actual / numero  
    else:
        print(f"Operación desconocida: {operacion}")
        return numero_actual
    

#variables necesarias para que el loop funcione
numero_actual = 0
puerto_actual = 1337


#loop que une las tres funciones y hace que el script funcione
while True:
    respuesta = consulta_puerto(puerto_actual)
    if respuesta is None:
        time.sleep(0.5)  # Espera un medio segundo antes de intentar nuevamente
        continue 

    resultado = parsear_respuesta(respuesta)
    if resultado is None:
        print("Proceso terminado. Número final:", round(numero_actual, 2))
        break

    operacion, numero, siguiente_puerto = resultado
    numero_actual = realizar_operacion(numero_actual, operacion, numero)
    print(f"Puerto {puerto_actual}: {operacion} {numero} -> {numero_actual}")
    puerto_actual = siguiente_puerto