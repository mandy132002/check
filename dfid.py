def dfs(start, depth, path, visited):
    path.append(start)
    visited.add(start)
    
    if start == goal:
        return True, path
    
    if depth == 0:
        return False, None
    
    for neighbor, cost in graph[start].items():
        if neighbor not in visited:
            found, new_path = dfs(neighbor, depth - 1, path, visited)
            if found:
                return True, new_path
    
    path.pop()
    visited.remove(start)
    
    return False, None

def dfid(start):
    depth = 0
    
    while True:
        path = []
        visited = set()
        
        found, new_path = dfs(start, depth, path, visited)
        if found:
            cost = sum(graph[new_path[i]][new_path[i+1]] for i in range(len(new_path)-1))
            return new_path, cost
        
        depth += 1
        
        print('='*50)
        print('Depth:', depth)
        print('Open List:', path)
        print('Closed List:', visited)

graph = {
    'A': {'B': 9, 'C': 4},
    'B': {'C': 2, 'D':7, 'E':3},
    'C': {'D': 1, 'E':6},
    'D': {'E': 4,'F':8},
    'E': {'F':2},
    'F': {}

}
start_node, goal = 'A', 'F'
path, cost = dfid(start_node)
print('+'*50)
print('Path:', path)
print('Cost:', cost)