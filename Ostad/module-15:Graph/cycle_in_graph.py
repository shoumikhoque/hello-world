from concept.Graph.Graph import Graph


def detect_cycle_rec(g, node, visited, rec_node_stack):
    # Node was already in the recursion stack. Cycle found.
    if rec_node_stack[node]:
        return True
    if visited[node]:
        return False
    # Mark current node as visited and add to recursion stack
    visited[node] = True
    rec_node_stack[node] = True
    adj_list=g.adj_list[node]
    if adj_list is not None:
        current = adj_list.head
        while current is not None:
            # Pick adjacent node and call it recursively
            adj_node_val = current.val
            # If the node is visited again in the same recursion => Cycle found
            if detect_cycle_rec(g, adj_node_val, visited, rec_node_stack):
                return True
            current = current.next
    rec_node_stack[node] = False
    return False


def detect_cycle(g):
    visited=[False]* g.nodes
    rec_node_stack=[False]* g.nodes
    for node in range (g.nodes):
        if detect_cycle_rec(g,node,visited,rec_node_stack):
            return True
    return False


if __name__ == '__main__':
    A = 5
    edges_list = [[1, 2], [4, 1], [2, 4], [3, 4], [5, 2], [1, 3]]
    i = 0
    for i in range(len(edges_list)):

        g = Graph(A)
        for edge in edges_list[i]:
            g.add_edge(edge[0],edge[1])
        print(str(g))
        print("\n\t Output:", detect_cycle(g))
        print("-" * 100)
        i += 1