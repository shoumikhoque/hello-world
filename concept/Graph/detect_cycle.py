from concept.Graph.Graph import Graph
def detect_cycle(g, param):
    # traverse using DFS
    # if any node is found which already has visited[val]=True
    # this node is one of the answers which has created the cycle
    pass


if __name__ == '__main__':
    g=Graph(10)
    g.add_edge(0,1)
    g.add_edge(0,2)
    g.add_edge(1,3)
    g.add_edge(1, 5)
    g.add_edge(2, 4)
    g.add_edge(2, 6)
    g.add_edge(3, 7)
    g.add_edge(3, 8)
    g.add_edge(4, 9)
    g.add_edge(4, 5)
    g.add_edge(5, 7)
    g.add_edge(5, 6)
    g.add_edge(6, 8)
    g.add_edge(6, 9)
    g.add_edge(7,0)
    g.add_edge(8, 5)
    g.add_edge(7, 9)
    g.add_edge(9, 3)
    g.add_edge(9, 5)

    # print(str(g))
    print(detect_cycle(g,0))