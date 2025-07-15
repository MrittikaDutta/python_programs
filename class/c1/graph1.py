class Graph:
    def __init__(self):
        self.graph={}
    def add_node(self,node):
        if node not in self.graph:
            self.graph[node]=[]
    def add_edge(self,snode,enode):
        if snode in self.graph and enode in self.graph:
            self.graph[snode].append(enode)
    def display(self):
        for node in self.graph:
            print(f"{node} -> {'  '.join(self.graph[node])}")
my_graph = Graph()

while True:
    print("\nMenu:")
    print("1. Add Node")
    print("2. Add Edge")
    print("3. Display Graph")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        node = input("Enter node name: ")
        my_graph.add_node(node)
    elif choice == "2":
        start_node = input("Enter the starting node: ")
        end_node = input("Enter the ending node: ")
        my_graph.add_edge(start_node, end_node)
    elif choice == "3":
        print("\nGraph:")
        my_graph.display()
    elif choice == "4":
        break
    else:
        print("Invalid choice")
