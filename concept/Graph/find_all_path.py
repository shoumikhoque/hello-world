import copy  # For deep copy if needed

from concept.Graph.Graph import Graph


def find_all_paths_recursive(graph, source, destination, visited, path, paths):
    # Mark the current node as visited and store in path
    visited[source] = True
    path.append(source)
    # If current vertex is same as destination, then print
    # stores the current path in 2D list (Deep copy)
    if source == destination:
        paths.append(copy.deepcopy(path))
    else:
        # If current vertex is not destination
        # Recur for all the vertices adjacent to this vertex
        if graph.adj_list[source] is not None:
            current = graph.adj_list[source].head
            while current is not None:
                if not visited[current.val]:
                    find_all_paths_recursive(graph, current.val, destination, visited, path, paths)
                current=current.next
    # Remove current vertex from path[] and mark it as unvisited
    path.pop()
    visited[source] = False

def find_all_paths(graph, source, destination):
    # Mark all the vertices as not visited
    visited = [False] * (graph.nodes)
    # Create a list to store paths
    paths = []
    path = []
    # Call the recursive helper function to find all paths
    find_all_paths_recursive(graph, source, destination, visited, path, paths)
    return paths


# Main program to test above function
if __name__ == "__main__":

    g = Graph(6)
    g.add_edge(0, 1)
    g.add_edge(0, 2)
    g.add_edge(1, 3)
    g.add_edge(1, 4)
    g.add_edge(3, 5)
    g.add_edge(4, 5)
    g.add_edge(2, 5)

    source = 0
    destination = 5
    print(str(g))
    paths = find_all_paths(g, source, destination)
    print(paths)