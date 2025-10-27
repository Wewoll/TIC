import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import TP4_Funciones
import utils

probs = [0.5, 0.2, 0.3]
C1 = ["11", "010", "00"]
C2 = ["10", "001", "110", "010", "0000", "0001", "111", "0110", "0111"]
lista = [C1, C2]
i = 0

for codigos in lista:
    i += 1
    rendimiento, redundancia = TP4_Funciones.calculoRendimientoYRedundancia(codigos, utils.genProbabilidadesAlfOrdN(probs, i))
    print(f"η{i} = {rendimiento:.4f}\tR{i} = {redundancia:.4f}")