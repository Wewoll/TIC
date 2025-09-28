import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import TP3_Funciones

codigos = [
    ["==", "<", "<=", ">", ">=", "<>"],         # S1
    ["(", "[]", "]]", "([", "[()]", "([)]"],    # S2
    ["/", "*", "-", "*", "++", "+-"],           # S3
    [".,", ";", ",,", ":", "...", ",:;"],       # S4
]

probabilidades = [0.10, 0.50, 0.10, 0.20, 0.05, 0.05]

for idx, codigo in enumerate(codigos, start=1):
    entropia = TP3_Funciones.calculoEntropiaCP(codigo, probabilidades)
    longitud = TP3_Funciones.calculoLongitudMedia(codigo, probabilidades)
    print(f"Codigo {idx}\t Entropía: {entropia:.4f}\t Longitud media: {longitud:.1f}")