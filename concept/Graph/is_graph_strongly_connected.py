from concept.Graph.Graph import Graph
def is_strongly_connected(graph):
    """
    Finds if the graph is strongly connected or not
    :param graph: The graph
    :return: returns True if the graph is strongly connected, otherwise False
    """
    # Step 1: Do DFS traversal starting from the first vertex.
    result = graph.deapth_first_search(0)
    # If DFS traversal doesn't visit all vertices, then return false
    if graph.nodes != len(result):
        return False
    # Step 2: Create a reversed graph
    graph2 = graph.transpose()
    # Step 3: Do DFS for reversed graph starting from the first vertex.
    # Staring Vertex must be same starting point of first DFS
    result = graph2.deapth_first_search(0)
    # If all vertices are not visited in second DFS, then
    # return false
    if graph2.nodes != len(result):
        return False
    return True

if __name__ == "__main__":

    V = 5
    g1 = Graph(V)
    g1.add_edge(0, 1)
    g1.add_edge(1, 2)
    g1.add_edge(2, 3)
    g1.add_edge(2, 4)
    g1.add_edge(3, 0)
    g1.add_edge(4, 2)
    print("Yes" if is_strongly_connected(g1) else "No")
    g2 = Graph(V)
    g2.add_edge(0, 1)
    g2.add_edge(1, 2)
    g2.add_edge(2, 3)
    g2.add_edge(2, 4)
    print("Yes" if is_strongly_connected(g2) else "No")