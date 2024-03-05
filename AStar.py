import heapq

class Node:
    def __init__(self, position, parent=None, g=0, h=0):
        self.position = position
        self.parent = parent
        self.g = g  # Cost from the start node to this node
        self.h = h  # Heuristic (estimated cost from this node to the goal)
        self.f = self.g + self.h  # Total cost (f = g + h)

    def __lt__(self, other):
        return self.f < other.f

def astar(grid, start, goal):
    rows, cols = len(grid), len(grid[0])
    open_set = []
    closed_set = set()

    start_node = Node(start)
    goal_node = Node(goal)

    heapq.heappush(open_set, start_node)

    while open_set:
        current_node = heapq.heappop(open_set)

        if current_node.position == goal_node.position:
            path = []
            while current_node:
                path.append(current_node.position)
                current_node = current_node.parent
            return path[::-1]  # Reverse the path to get it from start to goal

        closed_set.add(current_node.position)

        for neighbor in get_neighbors(current_node.position, rows, cols):
            if neighbor in closed_set:
                continue

            g = current_node.g + 1  # Assuming a uniform cost of movement

            if neighbor not in [node.position for node in open_set]:
                h = heuristic(neighbor, goal)
                new_node = Node(neighbor, current_node, g, h)
                heapq.heappush(open_set, new_node)
            else:
                for node in open_set:
                    if node.position == neighbor:
                        if g < node.g:
                            node.g = g
                            node.f = g + node.h
                            node.parent = current_node

    return None  # No path found

def get_neighbors(position, rows, cols):
    row, col = position
    neighbors = []
    if row > 0:
        neighbors.append((row - 1, col))
    if row < rows - 1:
        neighbors.append((row + 1, col))
    if col > 0:
        neighbors.append((row, col - 1))
    if col < cols - 1:
        neighbors.append((row, col + 1))
    return neighbors

def heuristic(current, goal):
    return abs(current[0] - goal[0]) + abs(current[1] - goal[1])

# Example usage
grid = [
    [0, 0, 0, 0, 0],
    [0, 1, 1, 0, 0],
    [0, 0, 0, 1, 0],
    [0, 0, 0, 1, 0],
    [0, 0, 0, 0, 0]
]

start_position = (0, 0)
goal_position = (4, 4)

path = astar(grid, start_position, goal_position)

if path:
    print(f"Shortest Path: {path}")
else:
    print("No path found.")
