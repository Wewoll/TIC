import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import TP4_Funciones
import utils

codigo_1 = ["0100100", "0101000", "0010010", "0100000"]
codigo_2 = ["0100100", "0010010", "0101000", "0100001"]
codigo_3 = ["0110000", "0000011", "0101101", "0100110"]

codigos = [codigo_1, codigo_2, codigo_3]
i = 0

for codigo in codigos:
    i += 1
    dist_hamming, err_detectables, err_corregibles = TP4_Funciones.analizarCodigoHamming(codigo)
    print(f"\nCodigo {i}:")
    print(f"Distancia de Hamming: {dist_hamming}")
    print(f"Errores detectables: {err_detectables}")
    print(f"Errores corregibles: {err_corregibles}")