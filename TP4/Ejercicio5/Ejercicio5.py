import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import TP4_Funciones
import utils

omega = 0.7
probs = [omega, 1 - omega]


codigosHuffman = TP4_Funciones.algoritmoHuffman(probs)
codigosShannonFanoOrd2 = TP4_Funciones.algoritmoShannonFano(utils.genProbabilidadesAlfOrdN(probs, 2))
lista = [codigosHuffman, codigosShannonFanoOrd2]
i = 0

print(f"L1 = {utils.genLongitudesCodigos(codigosHuffman)}")
print(f"L2 = {utils.genLongitudesCodigos(codigosShannonFanoOrd2)}")
for codigos in lista:
    i += 1
    probsN = utils.genProbabilidadesAlfOrdN(probs, i)
    r = len(utils.genAlfabetoCodigos(codigos))

    print(f"\nn = {i}")
    print(f"H{r}(S) = {utils.calculoEntropia(probs, r):.2f}")
    print(f"L{i} = {utils.calculoLongitudMedia(codigos, probsN):.2f}")
    print(f"Cumple el Primer Teorema de Shannon: {TP4_Funciones.cumpleShannon(probs, codigos, i)}")