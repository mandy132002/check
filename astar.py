from queue import PriorityQueue
graph = {
    'A': {'B': 5, 'C': 10},
    'B': {'D': 5},
    'C': {'D': 10},
    'D': {'E': 5},
    'E': {}
}

heuristic = {
    'A': 20,
    'B': 15,
    'C': 10,
    'D': 5,
    'E': 0
}

def a_star(start, goal):
    open_list = PriorityQueue()
    open_list.put((0 + heuristic[start], start, 0))
    
    closed_list = {}
    
    cost = {start: 0}
    parent = {start: None}

    print('='*50)
    print('Open List:', list(open_list.queue))
    print('Closed List:', closed_list)
    print('Cost:', cost)
    print('Parent:', parent)
    
    while not open_list.empty():
        current_f, current_node, current_cost = open_list.get()
        
        closed_list[current_node] = (current_cost, heuristic[current_node])
        
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
            
            open_list.put((tentative_cost + heuristic[neighbor], neighbor, tentative_cost))
            
            cost[neighbor] = tentative_cost
            parent[neighbor] = current_node
        
        print('='*50)
        print('Open List:', list(open_list.queue))
        print('Closed List:', closed_list)
        print('Cost:', cost)
        print('Parent:', parent)
    
    return None

start_node = 'A'
goal_node = 'E'
path, cost = a_star(start_node, goal_node)
print('+'*50)
print('Path:', path)
print('Cost:', cost)