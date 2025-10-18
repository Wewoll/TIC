import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import utils

# Verifica si se cumple el Primer Teorema de Shannon (pasar codigos extendidos)
def cumpleShannon(probabilidades, codigos, N = 1):
    prob_ext = utils.genProbabilidadesAlfOrdN(probabilidades, N)
    long_media = utils.calculoLongitudMedia(codigos, prob_ext)
    entropia = utils.calculoEntropiaCP(codigos, probabilidades)

    long_media_norm = long_media / N
    lim_inf = entropia
    lim_sup = entropia + (1 / N)

    return  lim_inf <= long_media_norm < lim_sup