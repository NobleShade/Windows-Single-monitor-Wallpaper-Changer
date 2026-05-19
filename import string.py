import string
import random

longitud = int(input("Ingrese la longitud de la contraseña: "))

caracteres = string.ascii_letters + string.digits + string.punctuation

contraseña = ''.join(random.choice(caracteres) for _ in range(longitud))

print("Contraseña generada:", contraseña)