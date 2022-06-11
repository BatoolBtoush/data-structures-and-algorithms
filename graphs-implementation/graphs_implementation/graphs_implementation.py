class Node:
    def __init__(self, value):
        self.value = value


class Edge:
    def __init__(self, node, weight=0):
        self.node = node
        self.weight = weight


class Graph:
    def __init__(self):
        self.adjacency_list = {}


    def add_node(self, value):

        node = Node(value)
        self.adjacency_list[node] = []
        return node


    def add_edge(self, node1, node2, weight=0):

        if not (node1 in self.adjacency_list.keys()) or not (
            node2 in self.adjacency_list.keys()
        ):
            raise KeyError("One or more of the nodes is not in the graph")
        else:
            edge = Edge(node2, weight=weight)
            self.adjacency_list[node1].append(edge)



    def get_node(self):
        pass



    def get_neighbors(self, node):
        pass



    def size(self):

        return len(self.adjacency_list)



    def __str__(self):
        output = ""
        for node in self.adjacency_list.keys():
            output += f"{node.value} -> "

            for edge in self.adjacency_list[node]:
                output += f" {edge.node.value} ->"

            output += " None\n"
        return output
