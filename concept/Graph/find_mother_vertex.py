from concept.Graph.Graph import Graph

def perform_dfs(g:Graph, start,visited):
    visited[start]=True
    if g.adj_list[start] is not None :
        temp=g.adj_list[start].head
        while temp:
            if not visited[temp.val]:
                perform_dfs(g,temp.val,visited)
            temp=temp.next
def find_mother_vertex(g:Graph):
    visited=[False]*g.nodes
    last_v=0
    for i in range(g.nodes):
        if not visited[i]:
            perform_dfs(g,i,visited)
            last_v=i
    visited=[False]*g.nodes
    perform_dfs(g,last_v,visited)
    if any(not i for i in visited):
        return -1
    else:
        return last_v


if __name__ == '__main__':
    edges_list = [[[1,0],[2,0], [1, 2], [1, 3], [3, 4], [4, 5], [4, 6]]]
    i = 0
    for i in range(len(edges_list)):
        num_vertices = 7
        g = Graph(num_vertices)
        for edge in edges_list[i]:
            g.add_edge(edge[0], edge[1])
        print(str(g))
        print("\n\t Output:", find_mother_vertex(g))
        print("-" * 100)
        i += 1