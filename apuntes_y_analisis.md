# 📄 APUNTES Y ANÁLISIS

## 🔹 UNIDAD 2: FUENTES DE INFORMACIÓN

### `calculoEntropia(probabilidades)` (H)
* **Procedimiento:** Se obtiene calculando la esperanza matemática de la información propia de cada símbolo. Es la sumatoria de $p_i \cdot \log_r(1/p_i)$ para cada probabilidad en la distribución.
* **Análisis:**
    * Representa la **incertidumbre promedio** de la fuente o la cantidad de información promedio que aporta cada símbolo.
    * **Valor Máximo:** Se alcanza cuando la fuente es **equiprobable** (máxima incertidumbre).
    * **Valor Mínimo (0):** Ocurre si la fuente es determinística (un símbolo tiene probabilidad 1).

---

## 🔹 UNIDAD 4: CODIFICACIÓN Y COMPRESIÓN

### `cumpleShannon(probabilidades, codigos, N)`
* **Procedimiento:** Se calcula la entropía de la fuente $H(S)$ y la longitud media del código $L$ (suma de longitudes ponderadas por probabilidad). Se verifica si $L$ satisface el Primer Teorema: $H(S) \le L < H(S) + 1/N$.
* **Análisis:**
    * Si devuelve **True**, el código es eficiente y teóricamente posible.
    * Si $L < H(S)$, el código violaría el teorema (sería imposible decodificar sin pérdida).
    * Al aumentar la extensión $N$, la longitud media por símbolo se acerca asintóticamente a la entropía.

### `algoritmoHuffman(probabilidades)`
* **Procedimiento:**
    1. Se inicia con nodos hoja, uno para cada símbolo y su probabilidad.
    2. Se seleccionan los dos nodos con menor probabilidad.
    3. Se combinan en un nuevo nodo padre (suma de probabilidades). Se asigna '0' a uno y '1' al otro.
    4. Se repite hasta que queda un solo nodo raíz.
    5. El código es el camino desde la raíz hasta la hoja.
* **Análisis:**
    * Genera un código **óptimo** (de longitud media mínima) para una fuente dada.
    * Siempre es **instantáneo** (prefijo).
    * Asigna palabras cortas a símbolos probables y largas a símbolos improbables.

### `algoritmoShannonFano(probabilidades)`
* **Procedimiento:**
    1. Se ordenan las probabilidades de mayor a menor.
    2. **Recursividad:** Se divide la lista en dos subgrupos cuyas sumas de probabilidades sean lo más parecidas posible.
    3. Se asigna '0' al primer grupo y '1' al segundo.
    4. Se repite el proceso recursivamente para cada subgrupo hasta llegar a probabilidades individuales.
* **Análisis:**
    * Es un código eficiente, pero **no siempre es óptimo** (Huffman es igual o mejor).
    * Es **instantáneo** (prefijo).
    * La división recursiva busca equilibrar el árbol de códigos.

### `calculoRendimiento` ($\eta$) y `calculoRedundancia` ($R$)
* **Procedimiento:**
    * **Rendimiento:** Relación entre la entropía y la longitud media ($\eta = H(S) / L$).
    * **Redundancia:** El complemento del rendimiento ($1 - \eta$).
* **Análisis:**
    * **Rendimiento:** Indica qué porcentaje de los bits transmitidos lleva información real. Un valor cercano a 1 indica alta eficiencia (como en Huffman).
    * **Redundancia:** Indica el porcentaje de capacidad del canal desperdiciada o usada para protección/estructura.

### `calcularTasaCompresion(original, comprimido)`
* **Procedimiento:** Se divide el tamaño del mensaje original por el tamaño del mensaje codificado ($N = \text{Original} / \text{Comprimido}$).
* **Análisis:**
    * **Resultado > 1:** Compresión efectiva (ej: 1.5 significa que el original era 1.5 veces más grande).
    * **Resultado < 1:** Expansión de datos (el algoritmo fue ineficiente para esa fuente).

### `comprimirRLC(mensaje)` (Run Length Coding)
* **Procedimiento:** Se recorre la cadena contando "rachas" consecutivas del mismo carácter. Se reemplaza la secuencia por el par `(carácter, cantidad)`.
* **Análisis:**
    * Este método solo es eficiente en fuentes con **baja entropía** (alta redundancia, muchos símbolos repetidos).
    * En fuentes aleatorias, suele aumentar el tamaño del archivo (tasa < 1).

### `calculoHamming(codigos)` (Distancia $d$)
* **Procedimiento:** Se comparan todos los pares posibles de palabras código y se cuenta en cuántos bits difieren (XOR). La distancia $d$ es el **mínimo** de esas diferencias.
* **Análisis:**
    * Determina la capacidad de corrección del código.
    * **$d=1$:** No detecta errores.
    * **$d=2$:** Detecta 1 error, corrige 0.
    * **$d=3$:** Detecta 2 errores, corrige 1.

### `genBytearrayMatrizParidad` (Paridad 2D: VRC/LRC)
* **Procedimiento:** Se organiza el mensaje en una matriz de bits. Se añade una columna para la paridad de cada fila (longitudinal) y una fila para la paridad de cada columna (vertical/cruzada).
* **Análisis:**
    * Permite **detectar** múltiples errores cruzando la información de filas y columnas fallidas.
    * Permite **corregir** exactamente 1 bit de error identificando la intersección de la fila y columna incorrectas.

### `decodificarParidadMatriz(bytes)` (Corrección de Errores)
* **Procedimiento:**
    1. Desempaqueta la secuencia de bytes en una matriz de bits de $(N+1) \times 8$.
    2. Verifica la paridad (par) de cada fila de datos (1 a N) y de cada columna (0 a 7).
    3. Si detecta exactamente **1 fila y 1 columna** con error, identifica la intersección y "flippea" ese bit para corregirlo.
    4. Si detecta otros patrones de error (múltiples filas/columnas), reporta error incorregible.
* **Análisis:**
    * Implementa un **Código de Producto** (Paridad 2D).
    * **Poder:** A diferencia de la paridad simple, este método **sí puede corregir** un error (porque las coordenadas fila/columna lo localizan).
    * **Límite:** Solo garantiza corregir 1 bit. Si hay errores múltiples (ej: 2 bits en la misma fila), el sistema falla o detecta el error pero no puede corregirlo.

## 🔹 UNIDAD 5: CANALES DE INFORMACIÓN

### `genMatrizCanal` (Matriz Condicional $P(B|A)$)
* **Procedimiento:** Se cuentan las ocurrencias de cada par entrada-salida $(a_i, b_j)$ y se dividen por la cantidad total de veces que apareció la entrada $a_i$.
* **Análisis:**
    * Describe el comportamiento físico o **ruido** del canal.
    * Cada fila representa una entrada; cada columna una salida.
    * **Propiedad:** La suma de cada fila debe ser siempre 1.

### `calcularProbabilidadesSalida` ($P(B)$)
* **Procedimiento:** Se suman las **columnas** de la matriz de eventos simultáneos $P(A, B)$. Fórmula: $P(B_j) = \sum_i P(A_i, B_j)$.
* **Análisis:**
    * Indica la probabilidad de recibir cada símbolo de salida, independientemente de qué se envió.
    * En canales con ruido, la distribución de salida suele ser más "plana" (más entropía) que la de entrada debido a la dispersión.

### `calcularMatrizPosteriori` ($P(A|B)$)
* **Procedimiento:** Se aplica el **Teorema de Bayes**: $P(A_i|B_j) = \frac{P(A_i, B_j)}{P(B_j)}$. Se divide cada columna de la matriz simultánea por la probabilidad de salida correspondiente.
* **Análisis:**
    * Representa la certeza "hacia atrás": *Dado que recibí $B_j$, ¿qué tan seguro estoy de que enviaron $A_i$?*
    * Si una columna tiene un 1.0 y el resto 0, significa que ese símbolo de salida elimina toda incertidumbre (característica de canal sin ruido).

### `calcularMatrizSimultanea` ($P(A, B)$)
* **Procedimiento:** Se aplica la **Regla de la Multiplicación**: $P(A_i, B_j) = P(B_j|A_i) \cdot P(A_i)$. Se multiplica cada fila de la matriz del canal por su probabilidad a priori correspondiente.
* **Análisis:**
    * Representa la probabilidad de que ocurra el evento conjunto "se envió $A_i$ **Y** se recibió $B_j$".
    * Es la base para calcular todo lo demás ($P(B)$, $P(A|B)$, Entropía Afín).
    * La suma de todos los elementos de la matriz debe ser 1.

### `calcularEntropiasPosteriori` (Lista de $H(A|b_j)$)
* **Procedimiento:**
    1. Obtiene la matriz a posteriori $P(A|B)$.
    2. Recorre la matriz por **columnas** (cada columna corresponde a una salida $b_j$).
    3. Calcula la entropía individual de la distribución de probabilidad de esa columna.
* **Análisis:**
    * Devuelve una lista de valores. Cada valor representa la **incertidumbre específica** que queda sobre la entrada cuando se observa esa salida particular.
    * Si un valor de la lista es 0, significa que esa salida específica es "perfecta": si la recibo, sé exactamente qué se envió.
    * El promedio ponderado de esta lista (usando $P(B)$) es la Equivocación $H(A|B)$.

### `calcularEquivocacion` (Ruido: $H(A|B)$)
* **Procedimiento:** Es el promedio ponderado de las entropías de las **columnas** de la matriz a posteriori $P(A|B)$.
    * Relación: $H(A|B) = H(A,B) - H(B)$.
* **Análisis:**
    * Mide la **incertidumbre restante** sobre la entrada después de observar la salida.
    * **$H(A|B) = 0$:** Canal **Sin Ruido**. Observar la salida me dice exactamente qué se envió.
    * Si es alta, la salida no me sirve de mucho para adivinar la entrada.

### `calcularPerdida` ($H(B|A)$)
* **Procedimiento:** Es el promedio ponderado de las entropías de las **filas** de la matriz del canal $P(B|A)$.
    * Relación: $H(B|A) = H(A,B) - H(A)$.
* **Análisis:**
    * Mide la dispersión o incertidumbre sobre qué saldrá, dado que sé qué entré.
    * **$H(B|A) = 0$:** Canal **Determinante**. Si envío un símbolo, sé 100% qué va a salir.

### `calcularEntropiaAfin` ($H(A, B)$)
* **Procedimiento:** Se calcula la entropía de la matriz de probabilidades simultáneas $P(A, B)$ tratada como una única distribución.
* **Análisis:**
    * Mide la incertidumbre total del sistema (entrada + salida).
    * Siempre se cumple que $H(A,B) \le H(A) + H(B)$. (Solo es igual si son eventos independientes, o sea, un canal inútil).

### `calcularInformacionMutua` ($I(A;B)$)
* **Procedimiento:**
    * **Por definición:** Doble sumatoria de $P(A,B) \cdot \log(\frac{P(A,B)}{P(A)P(B)})$.
    * **Por relaciones:** $I(A;B) = H(A) - H(A|B)$ (Reducción de incertidumbre de entrada).
* **Análisis:**
    * Representa la **información útil** que logra atravesar el canal.
    * Es simétrica: $I(A;B) = I(B;A)$.
    * **Valor máximo:** Es la **Capacidad** del canal ($C$).
    * No puede ser negativa. Si es 0, la salida no tiene relación con la entrada.

## 🔹 UNIDAD 6: CANALES CON RUIDO (CAPACIDAD Y REDUCCIÓN)

### `esCanalSinRuido(matriz)`
* **Procedimiento:** Se verifica que cada **columna** de la matriz tenga exactamente un elemento distinto de cero.
* **Análisis:**
    * **Sin Ruido (Lossless):** Si sé la salida, sé la entrada con certeza.
    * La equivocación $H(A|B) = 0$.
    * La capacidad es $C = \log_2(\text{Nro de Entradas})$.

### `esCanalDeterminante(matriz)`
* **Procedimiento:** Se verifica que cada **fila** de la matriz tenga exactamente un elemento distinto de cero (que, por propiedad de probabilidad, debe ser 1.0).
* **Análisis:**
    * **Determinante (Deterministic):** Si sé la entrada, sé la salida con certeza.
    * La pérdida $H(B|A) = 0$.
    * La capacidad es $C = \log_2(\text{Nro de Salidas})$.

### `calcularMatrizCompuesta` (Canales en Serie)
* **Procedimiento:** Se realiza la **multiplicación de matrices**: $P(C|A) = P(B|A) \times P(C|B)$.
* **Análisis:**
    * Representa la probabilidad de transición total desde la entrada inicial hasta la salida final, sumando todos los caminos intermedios posibles.
    * Al conectar canales en serie, la información mutua tiende a disminuir ($I(A;C) \le I(A;B)$) y el ruido a aumentar.

### `verificarColumnasProporcionales` (Reducción Suficiente)
* **Procedimiento:** Se verifica si existe una constante $k$ tal que $Col_1 = k \cdot Col_2$ (o viceversa) para todas las filas de la matriz.
* **Análisis:**
    * Si dos columnas son proporcionales, aportan la misma información relativa sobre la entrada.
    * **Teorema:** Agrupar columnas proporcionales en una sola salida **no** reduce la Información Mutua ($I(A;B)$ se mantiene igual). Es una "Reducción Suficiente".
    * Permite simplificar el modelo del canal sin perder información.

### `genMatrizReduccion` (Matriz de Transformación)
* **Procedimiento:** Genera una matriz determinante $P(C|B)$ que mapea las columnas del canal original a un nuevo conjunto de columnas reducidas. Las dos columnas proporcionales se mapean a la misma salida (sumándose), y el resto se mapea 1 a 1.
* **Análisis:**
    * Es el operador matemático que realiza la reducción.
    * Al multiplicar el canal original por esta matriz ($P(B|A) \times P(C|B)$), se obtiene el canal reducido $P(C|A)$.

### `realizarReduccionMaxima`
* **Procedimiento:** Busca iterativamente pares de columnas proporcionales y aplica la reducción (usando `genMatrizReduccion` y multiplicación de matrices) hasta que no se pueden realizar más combinaciones.
* **Análisis:**
    * Transforma el canal en su versión más simple posible (mínima cantidad de salidas) sin perder Capacidad de Información.
    * Si la matriz resultante es cuadrada e identidad (o una permutación), significa que el canal original era equivalente a un canal sin ruido (aunque tuviera más salidas).

### `esCanalUniforme(matriz)`
* **Procedimiento:** Se verifica si todas las filas son **permutaciones** de la primera fila (es decir, tienen los mismos valores de probabilidad, aunque en distinto orden).
* **Análisis:**
    * En un canal uniforme, la "dispersión" del ruido es igual para cualquier símbolo de entrada.
    * La pérdida $H(B|A)$ es constante e igual a la entropía de cualquier fila.
    * La capacidad se calcula con la fórmula simplificada: $C = \log_2(\text{Salidas}) - H(\text{fila})$.

### `calcularCapacidadEspecial` (Atajos de Capacidad)
* **Procedimiento:** Clasifica el canal y aplica fórmulas simplificadas:
    * **Determinante:** $C = \log_2(\text{Salidas})$. (Porque $H(B|A)=0$).
    * **Sin Ruido:** $C = \log_2(\text{Entradas})$. (Porque $H(A|B)=0$).
    * **Uniforme:** $C = \log_2(\text{Salidas}) - H(\text{Fila})$.
* **Análisis:**
    * Estas fórmulas solo son válidas bajo las condiciones estrictas de simetría o determinismo del canal.
    * Permiten hallar $C$ sin necesidad de maximizar la Información Mutua numéricamente.

### `estimarCapacidadCanalBinario(matriz, paso)`
* **Procedimiento:** Realiza un barrido de fuerza bruta ("grid search"). Prueba diferentes probabilidades a priori $P(A) = [p, 1-p]$ variando $p$ desde 0 a 1 con el `paso` dado. Calcula $I(A;B)$ para cada una y se queda con el máximo.
* **Análisis:**
    * La **Capacidad ($C$)** se define como el máximo de la Información Mutua sobre todas las posibles distribuciones de entrada.
    * Este método numérico es necesario cuando el canal no es simétrico ni uniforme (no hay fórmula cerrada simple).
    * La precisión depende del tamaño del `paso`.

### `calcularProbabilidadError` ($P_E$ - Regla Máxima Posibilidad)
* **Procedimiento (Criterio Cátedra/Guía):**
    1. Se define una **Regla de Decisión Fija** basada únicamente en la matriz del canal: para cada columna (salida), se elige la fila (entrada) con la probabilidad de transición más alta ($P(b|a)$ máximo).
    2. Se calcula la probabilidad de error sumando las probabilidades $P(A, B)$ de todos los cruces que **no** fueron seleccionados por esa regla.
* **Análisis:**
    * Evalúa el desempeño del canal asumiendo una decisión basada en la "máxima verosimilitud" (suponiendo a priori equiprobable para la decisión, pero usando la a priori real para el cálculo del error).
    * Un $P_E$ bajo indica que el canal conserva bien la identidad de los símbolos.