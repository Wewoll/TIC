import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import TP3_Funciones

probs_f1 = [0.500, 0.250, 0.125, 0.125]
probs_f2 = [0.333, 0.333, 0.167, 0.167]

for i in range(2, 4):
    print(f"Longitudes ideales para la fuente 1 con alfabeto de tamano {i}: {TP3_Funciones.calculoLongitudIdeal(probs_f1, i)}")
    print(f"Longitudes ideales para la fuente 2 con alfabeto de tamano {i}: {TP3_Funciones.calculoLongitudIdeal(probs_f2, i)}")