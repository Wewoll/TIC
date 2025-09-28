import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import TP2_Funciones

matriz1 = [ [1/2, 0, 0, 0] ,
            [1/4, 0, 0, 1/2] ,
            [0, 1, 1, 0] ,
            [1/4, 0, 0, 1/2]
          ]

matriz2 = [ [1/2, 0, 0, 1/2] ,
            [1/2, 0, 0, 0] ,
            [0, 1/2, 0, 0] ,
            [0, 1/2, 1, 1/2]
          ]

matriz3 = [ [1/3, 0, 1, 1/2, 0] ,
            [1/3, 0, 0, 0, 0] ,
            [0, 1, 0, 0, 0] ,
            [1/3, 0, 0, 0, 1/2] ,
            [0, 0, 0, 1/2, 1/2]
          ]

grafos = [matriz1, matriz2, matriz3]


for idx, matriz in enumerate(grafos, start = 1):
    print(f"Grafo {idx}:")
    ergodica = TP2_Funciones.esFuenteErgodica(matriz)
    print(f"  Ergodica: {ergodica}")
    if ergodica:
        vector_est = TP2_Funciones.genVectorEstacionario(matriz)
        entropia = TP2_Funciones.calculoEntropiaMarkov(matriz)
        print(f"  Vector estacionario: {vector_est}")
        print(f"  Entropía: {entropia:.2f}")