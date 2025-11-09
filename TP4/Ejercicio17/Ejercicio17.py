import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import TP4_Funciones
import utils

alfabeto = [
    ' ', ',', '.', ':', ';', 'A', 'B', 'C', 
    'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K',
    'L', 'M', 'N', 'Ñ', 'O', 'P', 'Q', 'R',
    'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'
]

probabilidades = [
    0.175990, 0.014093, 0.015034, 0.000542, 0.002109, 0.111066, 0.015368, 0.030176,
    0.038747, 0.101604, 0.004873, 0.008762, 0.007953, 0.049740, 0.003706, 0.000034,
    0.048149, 0.021041, 0.050490, 0.002018, 0.073793, 0.019583, 0.010246, 0.051446,
    0.058406, 0.031093, 0.033240, 0.008930, 0.000012, 0.000706, 0.007851, 0.003199
]

mensaje = "BUENAS TARDES, ESTO ES UNA PRUEBA DE COMPRENSION"

# Creacion de archivo
codigos_huffman = TP4_Funciones.algoritmoHuffman(probabilidades)
codigos_shannon_fano = TP4_Funciones.algoritmoShannonFano(probabilidades)

codificado_huffman = TP4_Funciones.codificarABytes(alfabeto, codigos_huffman, mensaje)
codificado_shannon_fano = TP4_Funciones.codificarABytes(alfabeto, codigos_shannon_fano, mensaje)

directorio_actual = os.path.dirname(os.path.abspath(__file__))
nombre_archivo = "mensaje_huffman.bin"
ruta_completa = os.path.join(directorio_actual, nombre_archivo)
with open(ruta_completa, "wb") as f:
    f.write(codificado_huffman)

nombre_archivo = "mensaje_shannon_fano.bin"
ruta_completa = os.path.join(directorio_actual, nombre_archivo)
with open(ruta_completa, "wb") as f:
    f.write(codificado_shannon_fano)

# Decodificacion del archivo
nombre_archivo = "mensaje_huffman.bin"
ruta_completa = os.path.join(directorio_actual, nombre_archivo)
with open(ruta_completa, "rb") as f:
    datos_huffman = f.read()

bytes_huffman = bytearray(datos_huffman)
mensaje_huffman = TP4_Funciones.decodificarDeBytes(alfabeto, codigos_huffman, bytes_huffman)
print(f"Mensaje (Huffman) recuperado: '{mensaje_huffman}'")

nombre_archivo = "mensaje_shannon_fano.bin"
ruta_completa = os.path.join(directorio_actual, nombre_archivo)
with open(ruta_completa, "rb") as f:
    datos_shannon_fano = f.read()

bytes_shannon_fano = bytearray(datos_shannon_fano)
mensaje_shannon_fano = TP4_Funciones.decodificarDeBytes(alfabeto, codigos_shannon_fano, bytes_shannon_fano)
print(f"Mensaje (Shannon-Fano) recuperado: '{mensaje_shannon_fano}'")