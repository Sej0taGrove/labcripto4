# cifrado_input.py

# Solicitud de clave en hexadecimal
key = input("Ingrese la clave en formato hexadecimal: ")

# Solicitud de IV en hexadecimal
iv = input("Ingrese el IV en formato hexadecimal: ")

# Solicitud de mensaje en texto claro
mensaje = input("Ingrese el mensaje a cifrar: ")

# Impresión de los datos ingresados para confirmar
print("\nDatos ingresados:")
print(f"Clave (hex): {key}")
print(f"IV (hex): {iv}")
print(f"Mensaje: {mensaje}")
