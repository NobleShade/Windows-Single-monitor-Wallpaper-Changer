import base64

print("Bienvenido al decodificador de Base64")

def funcion_decoder():
    with open("c:/Users/jdchm/OneDrive/Escritorio/Cositas Hacking/b64_1550406728131.txt", "r") as archivo: 
        contenido = archivo.read()
    decoded = base64.b64decode(contenido)
    for i in range(49):
        decoded = base64.b64decode(decoded).decode("utf-8")
    print("La cadena decodificada es: " + decoded)

funcion_decoder()