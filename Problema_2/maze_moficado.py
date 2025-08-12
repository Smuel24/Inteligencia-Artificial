import heapq


class Node:
    def __init__(self, position, parent=None, action=None, path_cost=0):
        self.position = position
        self.parent = parent
        self.action = action
        self.path_cost = path_cost

    def __lt__(self, other):
        return self.path_cost < other.path_cost



class Problem:
    def __init__(self, maze, start, goals):
        self.maze = maze
        self.start = start
        self.goals = goals
        self.actions = {
            (-1, 0): "Up",
            (1, 0): "Down",
            (0, -1): "Left",
            (0, 1): "Right"
        }

    def result(self, state, action):
        dx, dy = action
        return (state[0] + dx, state[1] + dy)

    def action_cost(self, state, action):
        """Costo por defecto: 1"""
        return 1

    def is_goal(self, state):
        return state in self.goals

    def in_bounds_and_free(self, state):
        x, y = state
        return (
            0 <= x < len(self.maze)
            and 0 <= y < len(self.maze[0])
            and self.maze[x][y] != "#"
        )


# Los costos
class ProblemWithCost(Problem):
    def action_cost(self, state, action):
        """Costo: 1 para espacio libre, 3 para terreno ~"""
        x, y = self.result(state, action)
        if self.maze[x][y] == "~":
            return 3
        return 1



def manhattan_distance(pos, goals):
    return min(abs(pos[0] - g[0]) + abs(pos[1] - g[1]) for g in goals)


def get_neighbors(problem, pos):
    neighbors = []
    for move, name in problem.actions.items():
        neighbor = problem.result(pos, move)
        if problem.in_bounds_and_free(neighbor):
            neighbors.append((neighbor, move, name))
    return neighbors


def reconstruct_path(node):
    path, actions = [], []
    while node:
        path.append(node.position)
        actions.append(node.action)
        node = node.parent
    path.reverse()
    actions.reverse()
    return path[1:], actions[1:]  


def find_exit(problem):
    start_node = Node(problem.start, path_cost=0)
    frontier = [(manhattan_distance(problem.start, problem.goals), start_node)]
    heapq.heapify(frontier)
    reached = {problem.start: start_node}

    while frontier:
        _, node = heapq.heappop(frontier)

        if problem.is_goal(node.position):
            return reconstruct_path(node)

        for neighbor_pos, move, action_name in get_neighbors(problem, node.position):
            new_cost = node.path_cost + problem.action_cost(node.position, move)
            if neighbor_pos not in reached or new_cost < reached[neighbor_pos].path_cost:
                reached[neighbor_pos] = Node(
                    neighbor_pos, parent=node, action=action_name, path_cost=new_cost
                )
                priority = new_cost + manhattan_distance(neighbor_pos, problem.goals)
                heapq.heappush(frontier, (priority, reached[neighbor_pos]))

    return None, None


# Laberindo modificado
maze_big = [
    ["#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#"],
    ["#", "S", " ", " ", "~", " ", " ", " ", " ", " ", "#"],
    ["#", " ", "#", " ", "#", "~", "#", " ", "#", " ", "#"],
    ["#", " ", "#", " ", "#", " ", "#", " ", "#", " ", "#"],
    ["#", " ", "#", " ", " ", " ", "~", " ", " ", " ", "#"],
    ["#", " ", "~", "#", "#", "#", "#", "#", "#", " ", "#"],
    ["#", " ", " ", " ", "~", " ", " ", " ", "#", "E", "#"],
    ["#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#"]
]

start = (1, 1)
goals = [(6, 9)]  # Salida


problem_big = ProblemWithCost(maze_big, start, goals)

path, actions = find_exit(problem_big)

print("Camino encontrado:", path)
print("Acciones:", actions)
