import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import TP2_Funciones

mensajes = [
    ("a", "CAAACCAABAACBBCABACCAAABCBBACC"),
    ("b", "BBAAACCAAABCCCAACCCBBACCAABBAA")
]
tolerancia = 0.1

for etiqueta, mensaje in mensajes:
    matriz = TP2_Funciones.genMatrizTransicion(mensaje)
    nula = TP2_Funciones.esFuenteSinMemoria(matriz, tolerancia = tolerancia)

    if nula:
        entropia = TP2_Funciones.calculoEntropia(TP2_Funciones.genProbabilidadesAlf(mensaje))
        tipo = "Fuente de memoria nula"
    else:
        vector_est = TP2_Funciones.genVectorEstacionario(matriz)
        entropia = TP2_Funciones.calculoEntropiaMarkov(matriz)
        tipo = "Fuente con memoria"

    print(f"{etiqueta}. {tipo} (tolerancia = {tolerancia}) H(S) = {entropia:.2f} bits")