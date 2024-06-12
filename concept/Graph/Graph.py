from concept.LinkedList.LinkedList import LinkedList


class AdjNode:
    def __init__(self,val):
        self.val=val
        self.next=None
class Graph:
    def __init__(self,v):
        self.nodes=v
        self.directed=True
        self.adj_list=[None]*(self.nodes)
        for i in range(v):
            self.adj_list[i]=LinkedList()
    def __str__(self):
        ans=''
        for i in range(len(self.adj_list)):
            # generate a full string for each node and then print line
            ans+="node: "+str(i)+" : " +str(self.adj_list[i])+'\n'
        return ans
    def add_edge(self, u, v):
        # add an edge from u to v for directed
        self.adj_list[u].add(v)
        # and v to u if undirected
        # self.adj_list[v].add(u)

    def remove_edge(self, u, v):
        # remove an edge from u to v for directed
        if self.adj_list[u] is  None:
            raise BaseException('No node '+ str(u))
        self.adj_list[u].remove_val(v)
        # try:
        #     self.adj_list[u].remove_val(v)
        # except BaseException as e:
            # print(e)
        # and v to u if undirected

    def add_node(self):
        self.nodes+=1
        self.adj_list.append(LinkedList())
    def removeNode(self):
        #
        pass
    def transpose(self):
        transpose_graph=Graph(self.nodes)
        for i in range(self.nodes):
            adj_node=self.adj_list[i].head
            while adj_node is not None:
                transpose_graph.add_edge(adj_node.val,i)
                adj_node=adj_node.next
        return transpose_graph

if __name__ == '__main__':
    g=Graph(8)
    g.add_edge(1, 2)
    g.add_edge(1, 3)
    g.add_edge(3, 4)
    print(str(g))
    # g.remove_edge(3,5)
    # print(str(g))
    g.add_node()
    g.add_edge(8, 9)
    print(str(g))

