class Node:
    def __init__(self, name, label, properties):
        self.name = name
        self.label = label
        self.properties = properties
        self.neighbors = {}

    def add_neighbor(self, relationship, node):
        self.neighbors[relationship] = node


class Graph:
    def __init__(self):
        self.nodes = {}

    def add_node(self, node):
        self.nodes[node.name] = node

    def add_edge(self, node1, relationship, node2):
        node1.add_neighbor(relationship, node2)
        node2.add_neighbor(relationship, node1)

# Create nodes
matrix = Node("The Matrix", "Movie", {"released": 1999})
a = Node("hasaa","hun",{"born":1999})
keanu = Node("Keanu Reeves", "Person", {})

# Add nodes to graph
graph = Graph()
graph.add_node(matrix)
graph.add_node(keanu)
graph.add_node(a)

# Add relationship between nodes
graph.add_edge(keanu, "ACTED_IN", matrix)


knrvs = graph.nodes['Keanu Reeves']
knrvs_neighbors = graph.nodes['Keanu Reeves'].neighbors

print(knrvs.name + " -> " + "ACTED_IN" +" -> " + knrvs_neighbors["ACTED_IN"].name)
