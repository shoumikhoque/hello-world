import copy
from concept.Graph.Graph import Graph
from concept.Stack.Stack import Stack


def connected_components(graph):
    """
    Function to find the connected components
    :param graph: The graph
    :return: returns a list of connected components
    """
    visited = [False]* graph.nodes
    result = []
    for v in range(graph.nodes):
        if not visited[v]:
            result.append(dfs(g, v, visited))
    return result

def dfs(g, source, visited):
    """
    Function to print a DFS of graph
    :param graph: The graph
    :param source: starting vertex
    :return: returns the traversal in a list
    """
    graph = copy.deepcopy(g)
    # Create a stack for DFS
    stack = Stack()
    # Result string
    result = []
    # Push the source
    stack.push(source)
    while not stack.is_empty():
        # Pop a vertex from stack
        source = stack.pop()
        if not visited[source]:
            result.append(source)
            visited[source] = True
        # Get all adjacent vertices of the popped vertex source.
        # If a adjacent has not been visited, then push it
        current=graph.adj_list[source].head
        while current is not None:
            if not visited[current.val]:
                stack.push((current.val))
            current=current.next
    return result
if __name__ == "__main__":

    g = Graph(7)
    g.add_edge(0, 1)
    g.add_edge(1, 2)
    g.add_edge(2, 3)
    g.add_edge(3, 0)
    g.add_edge(4, 5)
    g.add_edge(5, 6)

    result = connected_components(g)

    print("Following are connected components")
    print(result)