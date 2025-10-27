import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import TP4_Funciones
import utils

probs = [0.2, 0.15, 0.1, 0.3, 0.25]
cod1 = ["01", "111", "110", "101", "100"]
cod2 = ["00", "01", "10", "110", "111"]
cod3 = ["0110", "010", "0111", "1", "00"]
cod4 = ["11", "001", "000", "10", "01"]

codigos = [cod1, cod2, cod3, cod4]
i = 0

for cod in codigos:
    i += 1
    rendimiento, redundancia = TP4_Funciones.calculoRendimientoYRedundancia(cod, probs)
    print(f"η{i} = {rendimiento:.4f}\tR{i} = {redundancia:.4f}")