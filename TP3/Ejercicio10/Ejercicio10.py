import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import TP3_Funciones

codigos_7 = [
    ["011", "000", "010", "101", "001", "100"],         # S1
    ["110", "100", "101", "001", "110", "010"],         # S2
    ["10", "1100", "0101", "1011", "0", "110"],         # S3
    ["1101", "10", "1111", "1100", "1110", "0"],        # S4
    ["011", "0111", "01", "0", "011111", "01111"],      # S5
    ["1110", "0", "110", "1101", "1011", "10"],         # S6
]

codigos_8 = [
    ["==", "<", "<=", ">", ">=", "<>"],         # S1
    ["(", "[]", "]]", "([", "[()]", "([)]"],    # S2
    ["/", "*", "-", "*", "++", "+-"],           # S3
    [".,", ";", ",,", ":", "...", ",:;"],       # S4
]

for idx, codigo in enumerate(codigos_7, start = 1):
    print(f"Sumatoria de Kraft punto 7 - {idx}: {TP3_Funciones.calculoInecuacionKraft(codigo)}")

for idx, codigo in enumerate(codigos_8, start = 1):
    print(f"Sumatoria de Kraft punto 8 - {idx}: {TP3_Funciones.calculoInecuacionKraft(codigo)}")