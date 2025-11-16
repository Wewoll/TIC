import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import TP6_Funciones
import utils

matriz_canal_A = [
    [0.60, 0.40],
    [0.20, 0.80]
]

matriz_canal_B = [
    [0.25, 0.75],
    [0.90, 0.10]
]

matriz_canal_C = [
    [0.51, 0.49],
    [0.72, 0.28]
]

matriz_canal_D = [
    [0.77, 0.23],
    [0.20, 0.80]
]

matrices_lista = [matriz_canal_A, matriz_canal_B, matriz_canal_C, matriz_canal_D]
decimales = 4
paso = 0.0001

for i, matriz_canal in enumerate(matrices_lista, start=1):
    print(f"\n--- Canal {i} ---")

    capacidad_estimada, probabilidad_optima = TP6_Funciones.estimarCapacidadCanalBinario(matriz_canal, paso)
    print(f"Capacidad estimada (C): {capacidad_estimada:.{decimales}f} bits")
    print(f"Probabilidad optima (p): {probabilidad_optima:.{decimales}f}")