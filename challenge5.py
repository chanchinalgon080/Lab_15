test_results = []

def record_test(test_name, condition):
    emoji = "✅" if condition else "❌"
    test_results.append(f"{emoji} {test_name}")

class Graph:
    def __init__(self):
        self.adjacency_list = {}  # Dictionary to store graph structure

    def add_vertex(self, vertex):
        if vertex not in self.adjacency_list:
            self.adjacency_list[vertex] = []  # Add new vertex with empty adjacency list

    def add_edge(self, vertex1, vertex2):
        self.add_vertex(vertex1)  # Ensure vertex1 exists
        self.add_vertex(vertex2)  # Ensure vertex2 exists
        if vertex2 not in self.adjacency_list[vertex1]:
            self.adjacency_list[vertex1].append(vertex2)  # Add vertex2 as neighbor
        if vertex1 not in self.adjacency_list[vertex2]:
            self.adjacency_list[vertex2].append(vertex1)  # Add vertex1 as neighbor

    def get_degree(self, vertex):
        if vertex in self.adjacency_list:
            return len(self.adjacency_list[vertex])  # Degree = number of connections
        return 0  # If vertex doesn't exist, return 0

    def find_all_paths(self, start_vertex, end_vertex, max_length=None):
        def dfs(current, target, path):
            if max_length is not None and len(path) > max_length:
                return
            if current == target:
                paths.append(path[:])  # Found valid path
                return
            for neighbor in self.adjacency_list.get(current, []):
                if neighbor not in path:
                    path.append(neighbor)
                    dfs(neighbor, target, path)
                    path.pop()  # Backtrack

        paths = []
        if start_vertex in self.adjacency_list and end_vertex in self.adjacency_list:
            dfs(start_vertex, end_vertex, [start_vertex])
        return paths

    def get_connected_components(self):
        visited = set()
        components = []

        def dfs(v, component):
            visited.add(v)
            component.append(v)
            for neighbor in self.adjacency_list[v]:
                if neighbor not in visited:
                    dfs(neighbor, component)

        for vertex in self.adjacency_list:
            if vertex not in visited:
                component = []
                dfs(vertex, component)
                components.append(component)
        return components


# 🧪 Test Cases
def test_1_5():
    graph = Graph()

    # Build test graph
    graph.add_edge("Lima", "Cusco")
    graph.add_edge("Lima", "Arequipa")
    graph.add_edge("Cusco", "Arequipa")
    graph.add_edge("Trujillo", "Piura")  # Second component

    # 1.5.1 Degree calculation
    lima_degree = graph.get_degree("Lima")
    record_test("1.5.1 Degree calculation", lima_degree == 2)

    # 1.5.2 Multiple paths finding
    paths = graph.find_all_paths("Lima", "Arequipa", max_length=3)
    has_multiple_paths = len(paths) >= 2
    record_test("1.5.2 Multiple paths finding", has_multiple_paths)

    # 1.5.3 Connected components
    components = graph.get_connected_components()
    has_two_components = len(components) == 2
    record_test("1.5.3 Connected components", has_two_components)

    # 1.5.4 Empty graph analysis
    empty_graph = Graph()
    empty_components = empty_graph.get_connected_components()
    record_test("1.5.4 Empty graph analysis", empty_components == [])

    # 1.5.5 Non-existent vertex handling
    degree = graph.get_degree("NonExistent")
    record_test("1.5.5 Non-existent vertex handling", degree == 0)

# 🚀 Run Tests
test_1_5()

# 📋 Summary
for r in test_results:
    print(r)
