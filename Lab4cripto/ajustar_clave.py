# ajustar_clave.py

from Crypto.Random import get_random_bytes

def ajustar_clave(clave, tamano_necesario):
    # Convierte la clave de hexadecimal a bytes
    clave_bytes = bytes.fromhex(clave)

    # Ajusta la clave según el tamaño requerido
    if len(clave_bytes) < tamano_necesario:
        # Si la clave es muy corta, añade bytes aleatorios
        clave_bytes += get_random_bytes(tamano_necesario - len(clave_bytes))
    elif len(clave_bytes) > tamano_necesario:
        # Si la clave es muy larga, la trunca
        clave_bytes = clave_bytes[:tamano_necesario]

    # Muestra la clave ajustada
    print(f"Clave ajustada ({tamano_necesario * 8} bits): {clave_bytes.hex()}")

# Ejemplo de uso con distintos tamaños para DES (8 bytes), AES-256 (32 bytes) y 3DES (24 bytes)
if __name__ == "__main__":
    clave = input("Ingrese la clave en formato hexadecimal: ")

    print("\nAjuste para DES (56 bits / 8 bytes):")
    ajustar_clave(clave, 8)

    print("\nAjuste para AES-256 (256 bits / 32 bytes):")
    ajustar_clave(clave, 32)

    print("\nAjuste para 3DES (168 bits / 24 bytes):")
    ajustar_clave(clave, 24)
