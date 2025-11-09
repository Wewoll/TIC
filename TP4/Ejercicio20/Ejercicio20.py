import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import TP4_Funciones
import utils

mensaje_a = "XXXYZZZZ"
mensaje_b = "AAAABBBCCDAA"
mensaje_c = "UUOOOOAAAIEUUUU"

mensajes = [mensaje_a, mensaje_b, mensaje_c]
i = 96

for msj in mensajes:
    i += 1
    msj_comprimido = TP4_Funciones.comprimirRLC(msj)
    tasa = TP4_Funciones.calcularTasaCompresion(msj, msj_comprimido)
    print(f"Mensaje {chr(i)} comprimido: {tasa}")