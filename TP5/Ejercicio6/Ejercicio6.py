import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import TP5_Funciones
import utils

A = ['a', 'b', 'c']
B = ['1', '2','3']

# Probabilidades a priori P(A)
prob_A = [0.3, 0.3, 0.4]

# Probabilidades condicionales del canal P(B|A)
prob_ba_1a = 0.4
prob_ba_2a = 0.4
prob_ba_3a = 0.2
prob_ba_1b = 0.3
prob_ba_2b = 0.2
prob_ba_3b = 0.5
prob_ba_1c = 0.3
prob_ba_2c = 0.4
prob_ba_3c = 0.3

# P(ai/bj)
matriz_canal = [
    [0.4, 0.4, 0.2],
    [0.3, 0.2, 0.5], 
    [0.3, 0.4, 0.3]
]

# Eventos simultaneos
prob_sim_a1 = 0.12
prob_sim_a2 = 0.12
prob_sim_a3 = 0.16
prob_sim_b1 = 0.09
prob_sim_b2 = 0.06
prob_sim_b3 = 0.15
prob_sim_c1 = 0.12
prob_sim_c2 = 0.16
prob_sim_c3 = 0.12

# Matriz de probabilidades simultaneas P(ai,bj)
matriz_sim = [
    [0.12, 0.12, 0.16],
    [0.09, 0.06, 0.15],
    [0.12, 0.16, 0.12]
]

# Probabilidad de salida
prob_B = [0.33, 0.34, 0.33]

# Probabilidades a posteriori P(A|B)
prob_ab_a1 = 0.36
prob_ab_a2 = 0.35
prob_ab_a3 = 0.18
prob_ab_b1 = 0.27
prob_ab_b2 = 0.18
prob_ab_b3 = 0.45
prob_ab_c1 = 0.36
prob_ab_c2 = 0.47
prob_ab_c3 = 0.36

# Matriz de probabilidades a posteriori P(ai|bj)
matriz_posteriori = [
    [0.36, 0.35, 0.18],
    [0.27, 0.18, 0.45],
    [0.36, 0.47, 0.36]
]