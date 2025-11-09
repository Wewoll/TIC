import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import TP4_Funciones
import utils

# Calcula la tasa de compresion
def calcularTasaCompresion(msj_og, msj_bytes):
    tamano_original = len(msj_og)
    tamano_comprimido = len(msj_bytes)
    tasa_compresion = 0
    
    if tamano_comprimido != 0:
        tasa_compresion = tamano_original / tamano_comprimido

    return tasa_compresion