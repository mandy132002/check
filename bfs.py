from collections import deque

def bfs(graph, vertex, visited):
    queue = deque()
    queue.append(vertex)
    visited.add(vertex)
    
    while queue:
        vertex = queue.popleft()
        result.append(vertex)
        for neighbor in graph[vertex]:
            if neighbor not in visited:
                queue.append(neighbor)
                visited.add(neighbor)

result = []
graph = {'S': ['A', 'B', 'D'], 'A': ['B', 'G1'], 'B': ['A', 'C'], 'C':['S','G2','F'], 'D':['S', 'C', 'E'], 'E': ['G3'], 'F': ['D', 'G3'], 'G1': [], 'G2': [], 'G3': []}
bfs(graph, 'S', set())
print('->'.join(result))