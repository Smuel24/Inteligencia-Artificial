¿Cómo cambia el comportamiento del algoritmo si cambiamos lafunción de costo? 
Si cambiamos la función de costo asignando diferentes valores a las acciones el algoritmo modificará el orden en que explora los nodos.
Con un coste uniforme la heurística seria el principal factor de decisión.
Conun coste variable el algoritmo priorizará caminos más “baratos” aunque sean más largos en número de pasos

¿Qué sucede si hay múltiples salidas en el laberinto? ¿Cómo
podrías modificar el algoritmo para manejar esto? Plantea una
propuesta.

El algoritmo actual solo considera una salida. Con múltiples salidas podría elegir la primera encontrada aunque no sea la óptima y la propuesta seria definir los goal  como una lista de coordenadas de salida, modificar is_goal para aceptar cualquiera de ellas y ajustar la heurística para calcular la distancia mínima a cualquiera de esas salidas.

Modifica el laberinto por uno más grande y con otro tipo de
obstáculo además de paredes. ¿Qué limitación encuentras en el
algoritmo? 

En el laberinto más grande con obstáculos adicionales (~ con costo 3), el algoritmo sigue encontrando un camino válido evitando en lo posible las casillas de mayor costo, pero la heurística Manhattan no considera dichos costos, por lo que podría elegir rutas más cortas en pasos pero más caras en costo total
