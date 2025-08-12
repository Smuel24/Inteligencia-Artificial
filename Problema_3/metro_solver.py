# metro_solver.py

import time
import tracemalloc

# Clase para representar un nodo en el árbol de búsqueda
# Contiene el estado, el padre (para reconstruir la ruta) y la acción
class Node:
    def __init__(self, state, parent=None, action=None):
        self.state = state
        self.parent = parent
        self.action = action

    # Retorna la lista de estados desde el inicio hasta este nodo
    def path(self):
        node, p = self, []
        while node:
            p.append(node.state)
            node = node.parent
        return list(reversed(p))

# Clase que define el problema de búsqueda
class Problem:
    def __init__(self, initial, goal, graph):
        self.initial = initial
        self.goal = goal
        self.graph = graph

    # Retorna las acciones posibles desde un estado dado.
    def actions(self, state):
        return self.graph.get(state, [])

    # Verifica si un estado es el estado objetivo
    def goal_test(self, state):
        return state == self.goal

# --- Algoritmos de Búsqueda ---

# Algoritmo Breadth-First Search (BFS).
# Explora el grafo nivel por nivel
def breadth_first_search(problem):
    node = Node(problem.initial)
    if problem.goal_test(node.state):
        return node.path()

    frontier = [node]
    explored = {problem.initial}

    while frontier:
        node = frontier.pop(0)
        for action in problem.actions(node.state):
            child_state = action
            if child_state not in explored:
                child_node = Node(child_state, parent=node, action=action)
                if problem.goal_test(child_node.state):
                    return child_node.path()
                frontier.append(child_node)
                explored.add(child_state)
    return None

# Algoritmo Iterative Deepening Search (IDS).
# Realiza búsquedas en profundidad con límite incremental.
def iterative_deepening_search(problem):
    # Límite de profundidad arbitrario, suficiente para este problema.
    for depth in range(1, 100):
        result = depth_limited_search(problem, depth)
        if result is not None:
            return result
    return None

# Búsqueda en profundidad con un límite de profundidad.
# Es una función de ayuda para IDS.
def depth_limited_search(problem, limit):
    
    # Función recursiva interna para la búsqueda.
    def recursive_dls(node, problem, limit):
        if problem.goal_test(node.state):
            return node.path()
        elif limit == 0:
            
            return None
        else:
            for action in problem.actions(node.state):
                child_node = Node(action, parent=node, action=action)
                result = recursive_dls(child_node, problem, limit - 1)
                if result is not None:
                    return result
            return None

    return recursive_dls(Node(problem.initial), problem, limit)


# --- Ejecución y Comparación ---

# Este bloque se ejecuta solo si el script es invocado directamente.
if __name__ == "__main__":
    # Definición del mapa del metro como un grafo (lista de adyacencia).
    metro_map = {
        'A': ['B', 'C'],
        'B': ['A', 'D', 'E'],
        'C': ['A', 'F'],
        'D': ['B', 'G'],
        'E': ['B', 'H', 'I'],
        'F': ['C', 'J'],
        'G': ['D'],
        'H': ['E'],
        'I': ['E', 'J'],
        'J': ['F', 'I']
    }

    # Definición del problema: encontrar la ruta de A a J
    initial_station = 'A'
    goal_station = 'J'
    metro_problem = Problem(initial_station, goal_station, metro_map)

    print(f"Buscando la ruta más corta de '{initial_station}' a '{goal_station}'...\n")

    # --- Ejecutar y medir BFS ---
    tracemalloc.start()
    start_time_bfs = time.perf_counter()
    path_bfs = breadth_first_search(metro_problem)
    end_time_bfs = time.perf_counter()
    current_bfs, peak_bfs = tracemalloc.get_traced_memory()
    tracemalloc.stop()

    print("--- Breadth-First Search (BFS) ---")
    if path_bfs:
        print(f"Ruta encontrada: {' -> '.join(path_bfs)}")
        print(f"Número de paradas (acciones): {len(path_bfs) - 1}")
    else:
        print("No se encontró una ruta.")
    print(f"Tiempo de ejecución: {(end_time_bfs - start_time_bfs) * 1e6:.4f} microsegundos")
    print(f"Pico de memoria utilizada: {peak_bfs / 1024:.4f} KB\n")


    # --- Ejecutar y medir IDS ---
    tracemalloc.start()
    start_time_ids = time.perf_counter()
    path_ids = iterative_deepening_search(metro_problem)
    end_time_ids = time.perf_counter()
    current_ids, peak_ids = tracemalloc.get_traced_memory()
    tracemalloc.stop()

    print("--- Iterative Deepening Search (IDS) ---")
    if path_ids:
        print(f"Ruta encontrada: {' -> '.join(path_ids)}")
        print(f"Número de paradas (acciones): {len(path_ids) - 1}")
    else:
        print("No se encontró una ruta.")
    print(f"Tiempo de ejecución: {(end_time_ids - start_time_ids) * 1e6:.4f} microsegundos")
    print(f"Pico de memoria utilizada: {peak_ids / 1024:.4f} KB")