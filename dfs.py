def dfs(graph, vertex, visited):
    result.append(vertex)
    visited.add(vertex)
    for neighbor in graph[vertex]:
        if neighbor not in visited:
            dfs(graph, neighbor, visited)

result = []
graph = {'A': ['B', 'D'], 'B': ['C'], 'C': [], 'D': ['J'], 'J': []}
dfs(graph, 'A', set())
print('->'.join(result))