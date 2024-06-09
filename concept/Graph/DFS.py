from concept.Graph.Graph import Graph
from concept.Stack.Stack import Stack


def deapth_first_search(g:Graph, start:int):
    if g.adj_list[start] is None:
        return
    ans=[]
    visited=[False]*g.nodes
    stack=Stack()
    stack.push(start)
    visited[start]=True
    while not stack.is_empty() :
        current_val=stack.pop()
        ans.append(current_val)
        current_head= g.adj_list[current_val].head
        while current_head is not None:
            if not visited[current_head.val] :
                stack.push(current_head.val)
                visited[current_head.val]=True
            current_head=current_head.next
    return ans




if __name__ == '__main__':
    g=Graph(10)
    edges=[[0,1],[0,2],[1,3],
           [1,5],[2,4],[2,6],
           [3,7],[3,8],[4,9],
           [4,5],[5,7],[5,6],
           [6,8],[6,9],[7,0],
           [8,5],[7,9],[9,5]]
    for e in edges:
        g.add_edge(e[0],e[1])

    # print(str(g))
    print(deapth_first_search(g,0))