import heapq

class Node:
    def __init__(self, state, parent=None, action=None, path_cost=0):
        self.state = state
        self.parent = parent
        self.action = action
        self.path_cost = path_cost

    def __lt__(self, other):
        return self.path_cost < other.path_cost

def expand(problem, node):
    children = []
    for action in problem.actions(node.state):
        child_state = problem.result(node.state, action)
        cost = node.path_cost + problem.action_cost(node.state, action, child_state)
        child_node = Node(child_state, node, action, cost)
        children.append(child_node)
    return children

class Problem:
    def __init__(self, initial, goal, actions, result, action_cost, is_goal):
        self.initial = initial
        self.goal = goal
        self.actions = actions
        self.result = result
        self.action_cost = action_cost
        self.is_goal = is_goal

def best_first_search(problem, f):
    node = Node(state=problem.initial)
    frontier = [(f(node), node)]
    heapq.heapify(frontier)
    reached = {problem.initial: node}

    while frontier:
        _, node = heapq.heappop(frontier)
        if problem.is_goal(node.state):
            return node

        for child in expand(problem, node):
            s = child.state
            if s not in reached or child.path_cost < reached[s].path_cost:
                reached[s] = child
                heapq.heappush(frontier, (f(child), child))
    return None

def result(state, action):
    return action  # En este caso, la acción es el nombre del estado destino

def action_cost(state, action, result):
    return action_costs.get((state, action), float('inf'))

def is_goal(state):
    return state == goal

# estimación del costo desde cada ciudad a Bucharest (distancia en línea recta)
heuristic = {
    'Arad': 366,
    'Zerind': 374,
    'Oradea': 380,
    'Sibiu': 253,
    'Timisoara': 329,
    'Lugoj': 244,
    'Mehadia': 241,
    'Drobeta': 242,
    'Craiova': 160,
    'Rimnicu Vilcea': 193,
    'Fagaras': 176,
    'Pitesti': 100,
    'Bucharest': 0,
    'Giurgiu': 77,
    'Urziceni': 80,
    'Hirsova': 151,
    'Eforie': 161,
    'Vaslui': 199,
    'Iasi': 226,
    'Neamt': 234
}

def f(node):
    # f(n) = g(n) + h(n)
    return node.path_cost + heuristic.get(node.state, float('inf'))

initial = 'Arad'
goal = 'Bucharest'

actions = {
    'Arad': ['Sibiu', 'Timisoara', 'Zerind'],
    'Zerind': ['Oradea', 'Arad'],
    'Oradea': ['Sibiu', 'Zerind'],
    'Sibiu': ['Oradea', 'Fagaras', 'Rimnicu Vilcea', 'Arad'],
    'Timisoara': ['Lugoj', 'Arad'],
    'Lugoj': ['Mehadia', 'Timisoara'],
    'Mehadia': ['Drobeta', 'Lugoj'],
    'Drobeta': ['Craiova', 'Mehadia'],
    'Craiova': ['Rimnicu Vilcea', 'Pitesti', 'Drobeta'],
    'Rimnicu Vilcea': ['Sibiu', 'Craiova', 'Pitesti'],
    'Fagaras': ['Sibiu', 'Bucharest'],
    'Pitesti': ['Rimnicu Vilcea', 'Bucharest', 'Craiova'],
    'Bucharest': ['Fagaras', 'Pitesti', 'Giurgiu', 'Urziceni'],
    'Giurgiu': ['Bucharest'],
    'Urziceni': ['Bucharest', 'Hirsova', 'Vaslui'],
    'Hirsova': ['Urziceni', 'Eforie'],
    'Eforie': ['Hirsova'],
    'Vaslui': ['Urziceni', 'Iasi'],
    'Iasi': ['Neamt', 'Vaslui'],
    'Neamt': ['Iasi'],
}

action_costs = {
    ('Arad', 'Sibiu'): 140,
    ('Arad', 'Timisoara'): 118,
    ('Arad', 'Zerind'): 75,
    ('Zerind', 'Oradea'): 71,
    ('Oradea', 'Sibiu'): 151,
    ('Sibiu', 'Fagaras'): 99,
    ('Sibiu', 'Rimnicu Vilcea'): 80,
    ('Timisoara', 'Lugoj'): 111,
    ('Lugoj', 'Mehadia'): 70,
    ('Mehadia', 'Drobeta'): 75,
    ('Drobeta', 'Craiova'): 120,
    ('Craiova', 'Rimnicu Vilcea'): 146,
    ('Craiova', 'Pitesti'): 138,
    ('Rimnicu Vilcea', 'Pitesti'): 97,
    ('Fagaras', 'Bucharest'): 211,
    ('Pitesti', 'Bucharest'): 101,
    ('Bucharest', 'Giurgiu'): 90,
    ('Bucharest', 'Urziceni'): 85,
    ('Urziceni', 'Hirsova'): 98,
    ('Hirsova', 'Eforie'): 86,
    ('Urziceni', 'Vaslui'): 142,
    ('Vaslui', 'Iasi'): 92,
    ('Iasi', 'Neamt'): 87,
}

problem = Problem(initial, goal, lambda s: actions.get(s, []), result, action_cost, is_goal)
solution = best_first_search(problem, f)

if solution:
    path = []
    node = solution
    total_cost = solution.path_cost
    while node:
        path.append(node.state)
        node = node.parent
    path.reverse()
    print("Solution path:", path)
    print(f"Total path cost: {total_cost}")
else:
    print("No solution found")

