import heapq

directed_graph = {
    'A': ['B', 'C'],
    'B': ['D'],
    'C': ['E'],
    'D': ['F'],
    'E': [],
    'F': [],
    'G': []
}

undirected_graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D'],
    'C': ['A', 'E'],
    'D': ['B', 'F'],
    'E': ['C'],
    'F': ['D'],
    'G': []
}

weighted_graph = {
    'A': {'B': 2, 'C': 4},
    'B': {'D': 7},
    'C': {'E': 3},
    'D': {'F': 1},
    'E': {},
    'F': {},
    'G': {}
}

def find_neighbors(graph, node):
    return graph.get(node, [])

def edge_exists(graph, node1, node2):
    return node2 in graph.get(node1, [])

def dijkstra(graph, start, end):
    queue = [(0, start)]
    distances = {node: float('inf') for node in graph}
    distances[start] = 0
    shortest_path = {node: None for node in graph}

    while queue:
        (cost, current_node) = heapq.heappop(queue)

        if current_node == end:
            path = []
            while current_node:
                path.insert(0, current_node)
                current_node = shortest_path[current_node]
            return path, cost

        for neighbor, weight in graph[current_node].items():
            distance = cost + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                shortest_path[neighbor] = current_node
                heapq.heappush(queue, (distance, neighbor))

    return None, float('inf')

print("Directed Graph Neighbors:")
print("Neighbors of node 'A':", find_neighbors(directed_graph, 'A'))
print("Does edge from 'A' to 'B' exist?", edge_exists(directed_graph, 'A', 'B'))

print("\nUndirected Graph Neighbors:")
print("Neighbors of node 'A':", find_neighbors(undirected_graph, 'A'))
print("Does edge from 'A' to 'C' exist?", edge_exists(undirected_graph, 'A', 'C'))

print("\nWeighted Graph Shortest Path:")
shortest_path, total_cost = dijkstra(weighted_graph, 'A', 'F')
if shortest_path:
    print(f"Shortest path from 'A' to 'F': {shortest_path} with total cost {total_cost}")
else:
    print("No path found from 'A' to 'F'")
