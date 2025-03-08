# PassGen
import string
import secrets

# Definir los caracteres a usar
letras = string.ascii_letters
digitos = string.digits
simbolos = "@?!$&"
alfabeto = letras + digitos

# Establecer la longitud de la contraseña
pwd_length = 12

# Asegurarse de que haya exactamente 2 símbolos
pwd = []
pwd += [secrets.choice(simbolos) for i in range(2)]  # 2 símbolos obligatorios

# Completar el resto de la contraseña con letras y dígitos
pwd += [secrets.choice(alfabeto) for i in range(pwd_length - 2)]  # Resto sin símbolos

# Barajar los caracteres para que los símbolos no siempre estén al principio
secrets.SystemRandom().shuffle(pwd)

# Convertir la lista a string
password = ''.join(pwd)

print(password)
