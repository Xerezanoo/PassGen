# PassGen
import string
import secrets

# Configuración
pwd_length = 18
num_simbolos = 2
num_digitos = 2

# Caracteres disponibles
letras = string.ascii_letters
digitos = string.digits
simbolos = "@?!$&"

# Generar partes obligatorias
pwd = []
pwd += [secrets.choice(simbolos) for _ in range(num_simbolos)]
pwd += [secrets.choice(digitos) for _ in range(num_digitos)]
pwd += [secrets.choice(letras) for _ in range(5)]  # Asegurar al menos 5 letras

# Rellenar el resto con letras, dígitos y símbolos mezclados
restantes = pwd_length - len(pwd)
alfabeto_completo = letras + digitos + simbolos
pwd += [secrets.choice(alfabeto_completo) for _ in range(restantes)]

# Barajar para aleatorizar
secrets.SystemRandom().shuffle(pwd)

# Resultado final
password = ''.join(pwd)
print(password)
