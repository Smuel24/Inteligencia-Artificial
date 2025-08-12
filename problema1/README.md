# A* Search para Ruta Óptima de Arad a Bucharest

## Análisis del problema

El problema consiste en encontrar la ruta más corta (de menor costo) desde la ciudad de Arad hasta Bucharest, en un mapa simplificado de carreteras entre ciudades rumanas. Cada conexión tiene un costo (distancia en kilómetros).

Este problema es un clásico problema de búsqueda en grafos, donde cada nodo es una ciudad, las aristas son carreteras con costos asociados, y el objetivo es minimizar el costo total de la ruta desde el nodo inicial (Arad) al nodo objetivo (Bucharest).

## Cómo se aplica A*

A* es un algoritmo de búsqueda informada que utiliza una función de evaluación para decidir qué nodo expandir primero. La función de evaluación es:

$$
f(n) = g(n) + h(n)
$$

- \(g(n)\): costo acumulado desde el nodo inicial hasta el nodo \(n\).
- \(h(n)\): heurística que estima el costo mínimo desde el nodo \(n\) hasta el nodo objetivo.

En este problema, \(g(n)\) es la suma de las distancias de las carreteras recorridas y \(h(n)\) es la distancia en línea recta estimada desde la ciudad actual a Bucharest (distancia heurística).

La heurística usada es admisible, es decir, nunca sobreestima el costo real, lo que garantiza que A* encuentra la ruta óptima.

## ¿Por qué la ruta encontrada es óptima?

Dado que la heurística es admisible y consistente (distancia en línea recta), A* explora los nodos de manera eficiente sin pasar por caminos innecesarios y garantiza que cuando encuentra el objetivo, la ruta es la de menor costo posible.

Por lo tanto, la ruta que devuelve el algoritmo es la ruta óptima desde Arad hasta Bucharest, con el menor costo total acumulado.

---

