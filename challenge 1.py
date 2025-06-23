# List to store test results with pass/fail status
test_results = []

# Helper function to record the result of a test
def record_test(test_name, condition):
    # Use emoji to indicate test result, append to test_results list
    emoji = "✅" if condition else "❌"
    test_results.append(f"{emoji} {test_name}")

# Definition of Graph class using adjacency list
class Graph:
    def __init__(self):
        # Initialize an empty dictionary to store the adjacency list
        self.adjacency_list = {}

    def get_vertices(self):
        # Return a list of all vertex names (keys of the adjacency list)
        return list(self.adjacency_list.keys())

    def get_vertex_count(self):
        # Return the number of vertices in the graph
        return len(self.adjacency_list)

    def has_vertex(self, vertex):
        # Return True if vertex exists in adjacency list, else False
        return vertex in self.adjacency_list

# Function to test various functionalities of the Graph class
def test_1_1():
    # 1.1.1 Test that a newly created graph has no vertices
    graph = Graph()
    record_test("1.1.1 Empty graph initialization", graph.get_vertex_count() == 0)

    # 1.1.2 Manually add vertices by modifying adjacency_list directly and count them
    graph.adjacency_list = {"Lima": [], "Cusco": []}
    record_test("1.1.2 Vertex counting", graph.get_vertex_count() == 2)

    # 1.1.3 Check if the vertex "Lima" exists
    record_test("1.1.3 Vertex existence check", graph.has_vertex("Lima") == True)

    # 1.1.4 Ensure that querying an empty graph works without error
    empty_graph = Graph()
    record_test("1.1.4 Empty graph edge case", empty_graph.has_vertex("Lima") == False)

    # 1.1.5 Confirm that get_vertices() returns a list
    record_test("1.1.5 Type validation", isinstance(graph.get_vertices(), list))

# Run the test cases
test_1_1()

# Print the summary of all test results
for r in test_results:
    print(r)
