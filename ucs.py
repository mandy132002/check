from queue import PriorityQueue

def ucs(start, goal):
    open_list = PriorityQueue()
    open_list.put((0, start))

    closed_list = {}

    print('='*50)
    print('Open List:', [(node, cost) for (cost, node) in list(open_list.queue)])
    print('Closed List:', closed_list)

    cost = {start: 0}
    parent = {start: None}

    while not open_list.empty():
        current_cost, current_node = open_list.get()

        closed_list[current_node] = current_cost

        if current_node == goal:
            path = []
            while current_node is not None:
                path.append(current_node)
                current_node = parent[current_node]
            path.reverse()
            return path, cost[goal]

        for neighbor, neighbor_cost in graph[current_node].items():
            tentative_cost = current_cost + neighbor_cost

            if neighbor in closed_list:
                continue

            if neighbor in cost and tentative_cost >= cost[neighbor]:
                continue

            open_list.put((tentative_cost, neighbor))

            cost[neighbor] = tentative_cost
            parent[neighbor] = current_node

        print('='*50)
        print('Open List:', [(node, cost) for (cost, node) in list(open_list.queue)])
        print('Closed List:', closed_list)

    return None


graph = {
    'A': {'B': 9, 'C': 4},
    'B': {'C': 2, 'D': 7, 'E': 3},
    'C': {'D': 1, 'E': 6},
    'D': {'E': 4, 'F': 8},
    'E': {'F': 2},
    'F': {}
}

path, cost = ucs('A', 'F')
print('Path:', path)
print('Cost:', cost)