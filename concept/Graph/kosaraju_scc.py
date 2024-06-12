from concept.Graph.Graph import Graph
from concept.Stack.Stack import Stack


def dfs(g, start, visited, stack):
    visited[start]=True
    adj_node=g.adj_list[start].head
    while adj_node is not None:
        if not visited[adj_node.val]:
            dfs(g,adj_node.val,visited,stack)
        adj_node=adj_node.next
    stack.push(start)


def dfs_util(g,start, visited):
    visited[start]=True
    print(start,end=' ')
    adj_node = g.adj_list[start].head
    while adj_node is not None:
        if not visited[adj_node.val]:
            dfs_util(g, adj_node.val, visited)
        adj_node = adj_node.next


def find_sccs(g:Graph):
    stack=Stack()
    visited=[False]*g.nodes
    for i in range(g.nodes):
        if not visited[i]:
            dfs(g,i,visited,stack)
    transpose_graph=g.transpose()
    visited = [False] * g.nodes
    while not stack.is_empty():
        i= stack.pop()
        if not visited[i]:
            dfs_util(transpose_graph,i,visited)
            print()

if __name__ == "__main__":
    g = Graph(7)
    g.add_edge(0, 1)
    g.add_edge(1, 2)
    g.add_edge(2, 3)
    g.add_edge(3, 0)
    g.add_edge(4, 5)
    g.add_edge(5, 6)

    print("Strongly connected components are:")
    find_sccs(g)