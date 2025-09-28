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

for idx, codigo in enumerate(codigos, start = 1):
    print(f"El código S{idx} es {TP3_Funciones.tipoCodigo(codigo)}")