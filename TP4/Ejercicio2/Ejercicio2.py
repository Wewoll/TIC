import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import TP4_Funciones
import utils

probs = [0.3 , 0.1, 0.4, 0.2]
codigos = ["BA", "CAB", "A", "CBA"]

for i in range(1,3):
    codigosN = utils.genAlfabetoOrdN(codigos, i)
    probsN = utils.genProbabilidadesAlfOrdN(probs, i)
    r = len(utils.genAlfabetoCodigos(codigos))

    print(f"\nn = {i}")
    print(f"H{r}(S) = {utils.calculoEntropiaCP(codigos, probs):.2f}")
    print(f"L{i} = {utils.calculoLongitudMedia(codigosN, probsN):.2f}")
    print(f"Cumple el Primer Teorema de Shannon: {TP4_Funciones.cumpleShannon(probs, codigosN, i)}")