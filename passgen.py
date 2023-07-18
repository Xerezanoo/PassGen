# PassGen
import string
import secrets

# Voy a definir el alfabeto que voy a usar para generar las contraseñas
letras = string.ascii_letters
digitos = string.digits
caracteres_especiales = "@?"
alfabeto = letras + digitos + caracteres_especiales

# Ahora establezco la longitud de la contraseña
pwd_length = 12

# Ahora creamos la contraseña
pwd = ''
for i in range(pwd_length):
    pwd += ''.join(secrets.choice(alfabeto))

print(pwd)