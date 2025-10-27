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

# Algoritmo de Huffman (iterativo)
def algoritmoHuffman(probabilidades):
    items = [[prob, [idx]] for idx, prob in enumerate(probabilidades)]
    codigos = [''] * len(probabilidades)

    while len(items) > 1:
        items.sort(key=lambda x: x[0])
        prob_baja, simbolos_bajos = items.pop(0)
        prob_alta, simbolos_altos = items.pop(0)

        for idx in simbolos_bajos:
            codigos[idx] = '0' + codigos[idx]

        for idx in simbolos_altos:
            codigos[idx] = '1' + codigos[idx]

        nuevo_item = [prob_baja + prob_alta, simbolos_bajos + simbolos_altos]
        items.append(nuevo_item)

    return codigos

# Algoritmo de Shannon-Fano, inicializacion
def algoritmoShannonFano(probabilidades):
    items = [[prob, idx] for idx, prob in enumerate(probabilidades)]
    items.sort(key=lambda x: x[0], reverse = True)
    codigos = [''] * len(probabilidades)
    recursividadShannonFano(items, codigos)
    return codigos

# Algoritmo de Shannon-Fano, parte recursiva
def recursividadShannonFano(items, codigos, prefijo = ''):
    N = len(items)
    if N == 1:
        codigos[items[0][1]] = prefijo
    else:   
        suma_total = sum(nodo[0] for nodo in items)
        suma_mitad = suma_total / 2

        suma_parcial = 0
        punto_corte = 0
        min_diferencia = float('inf')

        for i in range(len(items) - 1):
            suma_parcial += items[i][0]
            diferencia = abs(suma_parcial - suma_mitad)
            if diferencia < min_diferencia:
                min_diferencia = diferencia
                punto_corte = i + 1

        grupo_superior = items[:punto_corte]
        grupo_inferior = items[punto_corte:]
        
        recursividadShannonFano(grupo_superior, codigos, prefijo + '1')
        recursividadShannonFano(grupo_inferior, codigos, prefijo + '0')

# Calculo del Rendimiento (η) y la Redundancia (1 - η)
def calculoRendimientoYRedundancia(codigos, probabilidades):
    entropia = utils.calculoEntropiaCP(codigos, probabilidades)
    long_media = utils.calculoLongitudMedia(codigos, probabilidades)

    rendimiento = entropia / long_media
    redundancia = 1 - rendimiento

    return rendimiento, redundancia