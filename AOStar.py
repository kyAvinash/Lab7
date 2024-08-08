class Graph:
    def __init__(self, graph, heuristic):
        self.graph = graph
        self.heuristic = heuristic
        self.solution_graph = {}

    def applyAOStar(self, node):
        if node not in self.solution_graph:
            self.solution_graph[node] = None

        if self.is_solution(node):
            return self.heuristic[node]

        min_cost = float('inf')
        for (successors, cost) in self.graph[node]:
            temp_cost = cost
            for successor in successors:
                temp_cost += self.applyAOStar(successor)

            if temp_cost < min_cost:
                min_cost = temp_cost
                self.solution_graph[node] = (successors, cost)

        return min_cost

    def is_solution(self, node):
        return len(self.graph[node]) == 0

    def print_solution(self, node):
        if self.solution_graph[node] is None:
            return

        successors, cost = self.solution_graph[node]
        print(f"{node} -> {successors} [Cost: {cost}]")
        for successor in successors:
            self.print_solution(successor)


# Define the AND-OR graph
graph = {
    'A': [(['B', 'C'], 1), (['D'], 3)],
    'B': [(['E'], 5), (['F'], 6)],
    'C': [(['G'], 7)],
    'D': [(['H'], 5)],
    'E': [],
    'F': [],
    'G': [],
    'H': []
}

# Define heuristic values for each node
heuristic = {
    'A': 10,
    'B': 12,
    'C': 4,
    'D': 7,
    'E': 3,
    'F': 8,
    'G': 2,
    'H': 5
}

# Instantiate and apply the AO* algorithm
g = Graph(graph, heuristic)
g.applyAOStar('A')
g.print_solution('A')
