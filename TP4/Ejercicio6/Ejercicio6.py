import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import TP4_Funciones
import utils

# Calculo del Rendimiento (η) y la Redundancia (1 - η)
def calculoRendimientoYRedundancia(codigos, probabilidades):
    entropia = utils.calculoEntropiaCP(codigos, probabilidades)
    long_media = utils.calculoLongitudMedia(codigos, probabilidades)

    rendimiento = entropia / long_media
    redundancia = 1 - rendimiento

    return rendimiento, redundancia