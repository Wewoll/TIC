import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import TP5_Funciones
import utils

A = [0, 1]
B = [0, 1]

# Probabilidades a priori P(A)
prob_A = [0.5, 0.5]

# Probabilidades condicionales del canal P(B|A)
prob_ba_00 = 1.0
prob_ba_10 = 0.0
prob_ba_01 = 0.0
prob_ba_11 = 1.0

# P(bi/aj)
matriz_canal = [
    [1.0, 0.0],
    [0.0, 1.0]
]

# Eventos simultaneos
prob_sim_00 = 0.5
prob_sim_10 = 0.0
prob_sim_01 = 0.0
prob_sim_11 = 0.5

# Matriz de probabilidades simultaneas P(ai,bj)
matriz_sim = [
    [0.5, 0.0],
    [0.0, 0.5]
]

# Probabilidad de salida
prob_B = [0.5, 0.5]

# Probabilidades a posteriori P(A|B)
prob_ab_00 = 1.0
prob_ab_10 = 0.0
prob_ab_01 = 0.0
prob_ab_11 = 1.0

# P(ai/bj)
matriz_posteriori = [
    [1.0, 0.0],
    [0.0, 1.0]
]