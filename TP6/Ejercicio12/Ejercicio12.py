import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import TP6_Funciones
import utils

matriz_canal = [
    [0.6, 0.4],
    [0.2, 0.8]
]
probs_priori = utils.genProbabilidadesEquiprobables(len(matriz_canal))
decimales = 4

prob_error = TP6_Funciones.calcularProbabilidadError(probs_priori, matriz_canal)
print(f"Probabilidad de error (P_e): {prob_error:.{decimales}f}")