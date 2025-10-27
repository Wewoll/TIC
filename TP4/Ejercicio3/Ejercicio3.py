import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import TP4_Funciones
import utils

probs = [0.5, 0.2, 0.3]
C1 = ["11", "010", "00"]
C2 = ["10", "001", "110", "010", "0000", "0001", "111", "0110", "0111"]
lista = [C1, C2]
i = 0

for codigos in lista:
    i += 1
    probsN = utils.genProbabilidadesAlfOrdN(probs, i)
    r = len(utils.genAlfabetoCodigos(codigos))

    print(f"\nn = {i}")
    print(f"H{r}(S) = {utils.calculoEntropia(probs, r):.2f}")
    print(f"L{i} = {utils.calculoLongitudMedia(codigos, probsN):.2f}")
    print(f"Cumple el Primer Teorema de Shannon: {TP4_Funciones.cumpleShannon(probs, codigos, i)}")