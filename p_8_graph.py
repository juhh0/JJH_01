from collections import defaultdict, deque

class Graph:
    def __init__(self, vertices):
        self.graph = defaultdict(list)  # adjacency list
        self.vertices = vertices

    def add_edge(self, u, v):
        self.graph[u].append(v)
        self.graph[v].append(u)

    def dfs(self, start):
        visited = set()
        result = []

        def dfs_recursive(node):
            visited.add(node)
            result.append(node)
            for neighbor in sorted(self.graph[node]):  # Sort for consistent order
                if neighbor not in visited:
                    dfs_recursive(neighbor)

        dfs_recursive(start)
        return result

    def bfs(self, start):
        visited = set()
        queue = deque([start])
        result = []

        while queue:
            node = queue.popleft()
            if node not in visited:
                visited.add(node)
                result.append(node)
                queue.extend(sorted(self.graph[node]))  # Sort for consistent order

        return result

    def connected_components(self):
        visited = set()
        components = []

        for vertex in self.vertices:
            if vertex not in visited:
                component = []
                queue = deque([vertex])
                while queue:
                    node = queue.popleft()
                    if node not in visited:
                        visited.add(node)
                        component.append(node)
                        queue.extend(sorted(self.graph[node]))
                components.append(component)

        return components

    def spanning_tree(self, start):
        visited = set()
        edges = []
        queue = deque([(start, None)])  # (current_node, parent_node)

        while queue:
            node, parent = queue.popleft()
            if node not in visited:
                visited.add(node)
                if parent:
                    edges.append((parent, node))
                for neighbor in sorted(self.graph[node]):
                    if neighbor not in visited:
                        queue.append((neighbor, node))

        return edges


# 입력 처리
vertices = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
edges = ['A-B', 'A-C', 'B-D', 'C-D', 'C-E', 'D-F', 'E-H', 'E-G', 'G-H']

graph = Graph(vertices)
for edge in edges:
    u, v = edge.split('-')
    graph.add_edge(u, v)

# 결과 출력
print("Adjacency List:")
for vertex in vertices:
    print(f"{vertex}: {sorted(graph.graph[vertex])}")

dfs_result = graph.dfs('A')
print("\nDFS:", " - ".join(dfs_result))

bfs_result = graph.bfs('A')
print("BFS:", " - ".join(bfs_result))

connected_components = graph.connected_components()
print("\nConnected Components (BFS):")
for component in connected_components:
    print(" - ".join(component))

spanning_tree = graph.spanning_tree('A')
print("\nSpanning Tree Edges:")
for edge in spanning_tree:
    print(f"{edge[0]} - {edge[1]}")
