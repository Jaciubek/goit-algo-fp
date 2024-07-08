import heapq

class Graph:
    def __init__(self):
        self.edges = {}

    def add_edge(self, from_node, to_node, weight):
        if from_node not in self.edges:
            self.edges[from_node] = []
        if to_node not in self.edges:
            self.edges[to_node] = []
        self.edges[from_node].append((to_node, weight))
        self.edges[to_node].append((from_node, weight))  # If the graph is undirected

def dijkstra(graph, start):
    # Priority queue: (distance, vertex)
    priority_queue = [(0, start)]
    # Distances dictionary
    distances = {vertex: float('inf') for vertex in graph.edges}
    distances[start] = 0
    # Visited set
    visited = set()

    while priority_queue:
        current_distance, current_vertex = heapq.heappop(priority_queue)
        if current_vertex in visited:
            continue

        visited.add(current_vertex)

        for neighbor, weight in graph.edges[current_vertex]:
            distance = current_distance + weight

            # Use this path only when it is better
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))

    return distances

# Example usage
def main():
    g = Graph()
    g.add_edge('A', 'B', 5)
    g.add_edge('A', 'C', 5)
    g.add_edge('B', 'C', 2)
    g.add_edge('B', 'D', 7)
    g.add_edge('C', 'D', 1)

    start_vertex = (input("Enter the letter(type the upper letter in range A-D): "))
    shortest_paths = dijkstra(g, start_vertex)

    print(f"Shortest distances from {start_vertex}:")
    for vertex, distance in shortest_paths.items():
        print(f"Shortest distances to {vertex}: {distance}")

if __name__ == "__main__":
    main()