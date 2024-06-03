from concept.Graph.Graph import Graph
from concept.Queue.Queue import Queue


def breadth_first_search(g:Graph,start:int):
    ans=[]
    #use queue
    if g.adj_list[start] is None:
        return
    q=Queue()
    visited=[False]*g.nodes
    q.enqueue(start)
    # while queue is not empty dequeue and check if this value has a node in graph and if the node has adjacent nodes and push them to queue
    while q.is_empty() is False:
        current_val=q.dequeue()
        if visited[current_val]==False:
            visited[current_val]=True
            ans.append(current_val)
            current_adj_list=g.adj_list[current_val]
            if current_adj_list is not None:
                current_head=current_adj_list.head
                while current_head is not None:
                    q.enqueue(current_head.val)
                    current_head=current_head.next
    return ans


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
    # g.add_edge(7,0)
    g.add_edge(8, 5)
    g.add_edge(7, 9)
    g.add_edge(8, 5)
    g.add_edge(9, 3)
    g.add_edge(9, 5)

    # print(str(g))
    print(breadth_first_search(g,0))
