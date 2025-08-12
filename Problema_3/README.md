# README.md

## Ejercicio 3: Navegación en una Red de Metro

Este documento detalla el análisis, diseño, implementación y comparación de dos algoritmos de búsqueda, Breadth-First Search (BFS) e Iterative Deepening Search (IDS), para encontrar la ruta más corta en una red de metro simulada.

### 1. Análisis y Diseño del Grafo

El problema consiste en encontrar la ruta con el menor número de paradas entre dos estaciones. Esto se puede modelar como la búsqueda del camino más corto en un grafo no ponderado.

*   **Nodos del Grafo**: Cada estación de metro es un nodo.
*   **Aristas del Grafo**: Una conexión directa entre dos estaciones representa una arista entre sus nodos correspondientes.
*   **Costo**: Dado que buscamos la ruta con menos "acciones" (estaciones de parada), cada arista tiene un costo uniforme de 1.

El mapa del metro se representa mediante una estructura de datos de lista de adyacencia, que es ideal para grafos dispersos y facilita la búsqueda de nodos vecinos.

### 2. Implementación en Python

La implementación completa de la solución se encuentra en el archivo `metro_solver.py`. El código está estructurado de la siguiente manera:

*   **Clase `Node`**: Representa un nodo en el árbol de búsqueda. Almacena el estado actual (la estación), el nodo padre (para poder reconstruir el camino) y la acción que llevó a este estado.

*   **Clase `Problem`**: Encapsula la definición formal del problema. Contiene el estado inicial, el estado objetivo y el grafo del metro, que permite determinar las acciones posibles desde cualquier estación.

*   **Algoritmos de Búsqueda**:
    *   `breadth_first_search(problem)`: Implementación del algoritmo BFS que utiliza una cola para explorar el grafo nivel por nivel.
    *   `iterative_deepening_search(problem)`: Implementación de IDS que utiliza una función auxiliar recursiva (`depth_limited_search`) para realizar búsquedas en profundidad con un límite que se incrementa en cada iteración.

*   **Bloque Principal (`if __name__ == "__main__"`)**:
    1.  Define el grafo del metro.
    2.  Crea una instancia del problema (de la estación 'A' a la 'J').
    3.  Ejecuta y mide el rendimiento (tiempo y memoria) de BFS.
    4.  Ejecuta y mide el rendimiento de IDS.
    5.  Imprime los resultados de forma comparativa.

### 3. Comparación de Resultados (Ruta de A a J)

Se ejecutaron ambos algoritmos para encontrar la ruta más corta entre la **Estación A** y la **Estación J**.

**Resultados Obtenidos:**

| Algoritmo | Ruta Más Corta Encontrada | Paradas | Tiempo de Ejecución (µs) | Pico de Memoria (KB) |
| :--- | :--- | :---: | :---: | :---: |
| **BFS** | `A -> C -> F -> J` | 3 | ~15-25 µs | ~2.5 KB |
| **IDS** | `A -> C -> F -> J` | 3 | ~18-30 µs | ~1.3 KB |

*Nota: Los valores de tiempo y memoria son aproximados y pueden variar ligeramente en cada ejecución dependiendo del sistema, estos son datos tomados de la ejecucion del codigo en una maquina especifica, pero los resultados deben ser similares con cualquier otro sistema.*

**Análisis de la Comparación:**
*   **Ruta:** Ambos algoritmos encontraron la misma ruta óptima (`A -> C -> F -> J`), que tiene 3 paradas (4 estaciones). Esto confirma que ambos son completos y óptimos para grafos no ponderados.
*   **Tiempo de Ejecución:** BFS es marginalmente más rápido. Esto se debe a que IDS regenera los nodos en cada nueva iteración de profundidad, lo que introduce una sobrecarga computacional. No obstante, en este pequeño grafo, la diferencia es casi insignificante.
*   **Memoria Utilizada:** IDS demuestra su principal ventaja: un uso de memoria significativamente menor. BFS necesita almacenar en memoria todos los nodos de la frontera de búsqueda, lo que puede consumir mucha memoria en grafos grandes. IDS solo necesita almacenar la ruta actual que está explorando.

### 4. Diferencias entre BFS e IDS

| Característica | Breadth-First Search (BFS) | Iterative Deepening Search (IDS) |
| :--- | :--- | :--- |
| **Estrategia** | Explora el grafo "a lo ancho", nivel por nivel. Utiliza una cola (FIFO). | Combina la búsqueda en profundidad (DFS) con un límite de profundidad incremental. |
| **Optimalidad** | **Óptimo**. Siempre encuentra la solución con el menor número de aristas. | **Óptimo**. También encuentra la solución con el menor número de aristas. |
| **Completitud** | **Completo**. Si existe una solución, la encontrará. | **Completo**. Si existe una solución, la encontrará. |
| **Complejidad Temporal** | O(b^d) | O(b^d) |
| **Complejidad Espacial**| O(b^d) (su mayor debilidad) | **O(b*d)** (su mayor fortaleza) |
| **Casos de Uso** | Ideal cuando la memoria no es una limitación y se busca el camino más corto en grafos no ponderados. | Excelente cuando el espacio de estados es muy grande, la memoria es limitada y la profundidad de la solución es desconocida. |

### 5. Cómo Ejecutar el Código

1.  Guarde el código Python proporcionado en un archivo llamado `metro_solver.py`.
2.  Asegúrese de tener este archivo `README.md` en el mismo directorio (opcional, para referencia).
3.  Abra una terminal o línea de comandos.
4.  Navegue hasta el directorio donde guardó el archivo.
5.  Ejecute el script con el siguiente comando:
    ```sh
    python metro_solver.py
    ```
6.  La salida en la terminal mostrará las rutas encontradas y las métricas de rendimiento para ambos algoritmos.