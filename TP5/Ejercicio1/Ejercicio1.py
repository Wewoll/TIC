import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import TP5_Funciones
import utils

A = ['a', 'b', 'c']
B = ['0', '1']

entrada = "abcacaabbcacaabcacaaabcaca"
salida  = "01010110011001000100010011"

total_simbolos = 26
total_a = 13
total_b = 5
total_c = 8

# Probabilidades a priori
p_a = 13/26
p_b = 5/26
p_c = 8/26

a_0 = 7
a_1 = 6
b_0 = 3
b_1 = 2
c_0 = 5
c_1 = 3

p_0_a = 7/13
p_1_a = 6/13
p_0_b = 3/5
p_1_b = 2/5
p_0_c = 5/8
p_1_c = 3/8

Matriz = [
    [7/13, 6/13], 
    [3/5, 2/5], 
    [5/8, 3/8],
]
