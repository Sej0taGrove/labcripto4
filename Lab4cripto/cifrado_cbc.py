# cifrado_cbc.py

from Crypto.Cipher import DES, AES, DES3
from Crypto.Util.Padding import pad, unpad

def cifrar_cbc(algoritmo, clave, iv, mensaje):
    # Validar que el tamaño del IV sea correcto para el algoritmo
    if len(iv) != algoritmo.block_size:
        raise ValueError(f"El IV debe tener {algoritmo.block_size} bytes para {algoritmo.name}")
    
    # Configura el cifrador en modo CBC
    cipher = algoritmo.new(clave, algoritmo.MODE_CBC, iv)
    mensaje_padded = pad(mensaje.encode(), algoritmo.block_size)
    mensaje_cifrado = cipher.encrypt(mensaje_padded)
    return mensaje_cifrado

def descifrar_cbc(algoritmo, clave, iv, mensaje_cifrado):
    # Validar que el tamaño del IV sea correcto para el algoritmo
    if len(iv) != algoritmo.block_size:
        raise ValueError(f"El IV debe tener {algoritmo.block_size} bytes para {algoritmo.name}")
    
    # Configura el descifrador en modo CBC
    cipher = algoritmo.new(clave, algoritmo.MODE_CBC, iv)
    mensaje_descifrado = unpad(cipher.decrypt(mensaje_cifrado), algoritmo.block_size)
    return mensaje_descifrado.decode()

# Solicitar datos de entrada
clave_hex = input("Ingrese la clave en formato hexadecimal: ")
iv_hex = input("Ingrese el IV en formato hexadecimal: ")
mensaje = input("Ingrese el mensaje a cifrar: ")

# Convertir clave y IV de hexadecimal a bytes
clave = bytes.fromhex(clave_hex)
iv = bytes.fromhex(iv_hex)

# Cifrado y descifrado con DES
print("\nCifrado con DES:")
try:
    mensaje_cifrado_des = cifrar_cbc(DES, clave[:8], iv[:8], mensaje)
    print("Mensaje cifrado (hex):", mensaje_cifrado_des.hex())
    mensaje_descifrado_des = descifrar_cbc(DES, clave[:8], iv[:8], mensaje_cifrado_des)
    print("Mensaje descifrado:", mensaje_descifrado_des)
except ValueError as e:
    print(e)

# Cifrado y descifrado con AES-256
print("\nCifrado con AES-256:")
try:
    mensaje_cifrado_aes = cifrar_cbc(AES, clave[:32], iv[:16], mensaje)
    print("Mensaje cifrado (hex):", mensaje_cifrado_aes.hex())
    mensaje_descifrado_aes = descifrar_cbc(AES, clave[:32], iv[:16], mensaje_cifrado_aes)
    print("Mensaje descifrado:", mensaje_descifrado_aes)
except ValueError as e:
    print(e)

# Cifrado y descifrado con 3DES
print("\nCifrado con 3DES:")
try:
    mensaje_cifrado_3des = cifrar_cbc(DES3, clave[:24], iv[:8], mensaje)
    print("Mensaje cifrado (hex):", mensaje_cifrado_3des.hex())
    mensaje_descifrado_3des = descifrar_cbc(DES3, clave[:24], iv[:8], mensaje_cifrado_3des)
    print("Mensaje descifrado:", mensaje_descifrado_3des)
except ValueError as e:
    print(e)
