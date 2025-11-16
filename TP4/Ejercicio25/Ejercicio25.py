import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import TP4_Funciones
import utils

# --- 1. Preparación de Datos ---

# (a) Datos de "CASA" (tomados de la imagen)
# Fila 0 (Paridad): 00100001 -> 33
# Fila 1 (C):      10000111 -> 135
# Fila 2 (A):      10000010 -> 130
# Fila 3 (S):      10100110 -> 166
# Fila 4 (A):      10000010 -> 130
bytes_25a_imagen = bytearray([33, 135, 130, 166, 130])

# (b) Datos de "LUNA" (tomados de la imagen)
# Fila 0 (Paridad): 00101101 -> 45
# Fila 1 (L):      10011001 -> 153
# Fila 2 (U):      10101010 -> 170
# Fila 3 (N):      10011100 -> 156
# Fila 4 (A):      10000010 -> 130
bytes_25b_imagen = bytearray([45, 153, 170, 156, 130])

# Mensajes originales esperados
mensaje_a = "CASA"
mensaje_b = "LUNA"

print("--- PRUEBA DE DECODIFICACIÓN (EJ 26b) ---")
print("Decodificando el bloque 'a' de la imagen...")
recuperado_a = TP4_Funciones.decodificarParidadMatriz(bytes_25a_imagen)
print(f"Resultado: '{recuperado_a}' (Esperado: '{mensaje_a}')\n")

print("Decodificando el bloque 'b' de la imagen...")
recuperado_b = TP4_Funciones.decodificarParidadMatriz(bytes_25b_imagen)
print(f"Resultado: '{recuperado_b}' (Esperado: '{mensaje_b}')\n")


print("--- PRUEBA DE CODIFICACIÓN (EJ 26a) ---")
print(f"Codificando el string '{mensaje_a}'...")
generado_a = TP4_Funciones.genBytearrayMatrizParidad(mensaje_a)
utils.imprimirBytearray(generado_a)
print(f"Generado:   {generado_a}")
print(f"De la imagen: {bytes_25a_imagen}")
print(f"Coinciden: {generado_a == bytes_25a_imagen}\n")

print(f"Codificando el string '{mensaje_b}'...")
generado_b = TP4_Funciones.genBytearrayMatrizParidad(mensaje_b)
utils.imprimirBytearray(generado_b)
print(f"Generado:   {generado_b}")
print(f"De la imagen: {bytes_25b_imagen}")
print(f"Coinciden: {generado_b == bytes_25b_imagen}\n")