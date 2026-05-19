 
import requests


def consulta_puerto(puerto):
    try:
        response = requests.get(f"http://10.65.156.145:{puerto}", timeout=3)
        return response.text
    except requests.exceptions.RequestException as e:
        print(f"Error al conectar al puerto {puerto}: {e}")
        return None

while True:
    prueba = consulta_puerto(1337)
    if prueba is None:
        continue
