import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import TP4_Funciones
import utils

# Genera un bytearray que contiene el mensaje con bits de paridad longitudinal, vertical y cruzada.
def genBytearrayMatrizParidad(mensaje):
    N = len(mensaje)
    matriz_bits = [[0] * 8 for _ in range(N + 1)]
    
    for i, caracter in enumerate(mensaje):
        valor_ascii_7bits = ord(caracter) & 0x7F
        bits_string = bin(valor_ascii_7bits)[2:].zfill(7)
        
        cantidad_de_unos = 0
        for j, bit in enumerate(bits_string):
            if bit == '1':
                matriz_bits[i + 1][j] = 1
                cantidad_de_unos += 1
        
        matriz_bits[i + 1][7] = cantidad_de_unos % 2
        

    for j in range(8):
        cantidad_de_unos = 0
        for i in range(1, N + 1):
            cantidad_de_unos += matriz_bits[i][j]
            
        matriz_bits[0][j] = cantidad_de_unos % 2
    
    resultado_bytes = bytearray()
    for i in range(N + 1):
        bits_fila = "".join(str(bit) for bit in matriz_bits[i])
        valor_byte = int(bits_fila, 2)
        resultado_bytes.append(valor_byte)
        
    return resultado_bytes


# Decodifica una secuencia de bytes (bytearray) con paridad
# Corrige un error simple y devuelve el mensaje ASCII recuperado o cadena vacía si no se puede corregir.
def decodificarParidadMatriz(secuencia_bytes):
    mensaje_recuperado = ""
    error_detectado = False
    error_incorregible = False

    # --- 1. Crear matriz de bits ---
    N_filas_total = len(secuencia_bytes)
    N_filas_datos = N_filas_total - 1
    matriz = []

    for byte in secuencia_bytes:
        bits = bin(byte)[2:].zfill(8)  # elimina '0b' y rellena a 8 bits
        matriz.append([int(b) for b in bits])

    # --- 2. Comprobación de paridades ---
    fila_fallida = -1
    col_fallida = -1
    errores_fila = 0
    errores_col = 0

    # Paridad horizontal (longitudinal)
    for i in range(1, N_filas_total):
        if sum(matriz[i]) % 2 != 0:
            fila_fallida = i
            errores_fila += 1

    # Paridad vertical (por columnas)
    for j in range(8):
        col_sum = sum(matriz[i][j] for i in range(N_filas_total))
        if col_sum % 2 != 0:
            col_fallida = j
            errores_col += 1

    # Paridad cruzada (esquina inferior derecha)
    bit_cruzado = matriz[0][7]
    total_unos = sum(sum(fila) for fila in matriz) - bit_cruzado
    cruzado_ok = (total_unos + bit_cruzado) % 2 == 0

    # --- 3. Análisis de errores ---
    if errores_fila == 0 and errores_col == 0 and cruzado_ok:
        # Caso 1: sin errores
        pass

    elif errores_fila == 1 and errores_col == 1 and not cruzado_ok:
        # Caso 2: error simple -> corregible
        bit_original = matriz[fila_fallida][col_fallida]
        matriz[fila_fallida][col_fallida] = 1 - bit_original
        error_detectado = True

    else:
        # Caso 3: error múltiple o inconsistente
        error_incorregible = True

    # --- 4. Reconstrucción del mensaje ---
    if not error_incorregible:
        chars = []
        for i in range(1, N_filas_total):
            bits_datos = matriz[i][:7]  # solo los 7 bits de datos
            ascii_val = int("".join(str(b) for b in bits_datos), 2)
            chars.append(chr(ascii_val))
        mensaje_recuperado = "".join(chars)

    # --- 5. Resultado final ---
    if error_incorregible:
        mensaje_recuperado = ""
    elif error_detectado:
        print(f"[Corrección] Error simple corregido en fila {fila_fallida}, columna {col_fallida}.")
    else:
        print("[OK] Sin errores detectados.")

    return mensaje_recuperado
