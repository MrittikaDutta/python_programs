import random

def contract(graph, u, v):
    # Contract edge (u, v) in the graph
    graph[u].extend(graph[v])
    for w in graph[v]:
        graph[w].remove(v)
        graph[w].append(u)
    graph[u] = list(filter(lambda x: x != u, graph[u]))

def min_cut(graph):
    while len(graph) > 2:
        u = random.choice(list(graph.keys()))
        v = random.choice(graph[u])
        contract(graph, u, v)
        del graph[v]
    return len(list(graph.values())[0])

def read_graph(filename):
    # Read the graph from the file
    graph = {}
    with open(filename, 'r') as file:
        for line in file:
            vertices = list(map(int, line.split()))
            graph[vertices[0]] = vertices[1:]
    return graph

def main():
    filename = 'input1.txt'  # Change this to your input file
    graph = read_graph(filename)
    
    # Set a seed for reproducibility (optional)
    random.seed(42)

    # Run the algorithm multiple times and find the minimum cut
    min_cut_value = float('inf')
    num_trials = 100  # Adjust the number of trials as needed

    for _ in range(num_trials):
        current_graph = {key: value.copy() for key, value in graph.items()}
        current_min_cut = min_cut(current_graph)
        min_cut_value = min(min_cut_value, current_min_cut)

    print("Minimum cut:", min_cut_value)

if __name__ == "__main__":
    main()
