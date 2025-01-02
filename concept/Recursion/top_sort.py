from concept.Graph.Graph import Graph
from concept.Stack.Stack import Stack


def helper(g:Graph, u, visited:list, result:list):
    visited[u]=True
    v=g.adj_list[u].head
    while v is not None:
        if visited[v.val] == False:
            helper(g, v.val, visited, result)
        v=v.next

    result.insert(0,u)

def top_sort(g:Graph):
    visited=[False]*g.nodes
    result=[]
    for u in range(g.nodes):
        if visited[u]==False:
            helper(g,u,visited,result)
    return result


if __name__ == '__main__':
    g=Graph(5)
    g.add_edge(0,1)
    g.add_edge(0,3)
    g.add_edge(1,2)
    g.add_edge(2,3)
    g.add_edge(2,4)
    g.add_edge(3,4)
    print(g)
    print(top_sort(g))
