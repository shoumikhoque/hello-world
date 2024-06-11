from concept.Graph.Graph import Graph
from concept.Queue.Queue import Queue


def check_if_path_exists_betweent_two_nodes(g:Graph,start,end):
    queue=Queue()
    queue.enqueue(start)
    visited=[False]*g.nodes
    while not queue.is_empty():
        current=queue.dequeue()
        visited[current] = True
        if current== end:
            return True
        current_adj_list=g.adj_list[current]
        if current_adj_list is not None:
            temp=current_adj_list.head
            while temp is not None:
                queue.enqueue(temp.val)
                temp=temp.next
    return False


if __name__ == '__main__':
    edges_list = [[[1,0],[2,0], [1, 2], [1, 3], [3, 4], [4, 5], [4, 6]]]
    i = 0
    for i in range(len(edges_list)):
        num_vertices = 7
        g = Graph(num_vertices)
        for edge in edges_list[i]:
            g.add_edge(edge[0], edge[1])
        print(str(g))
        print("\n\t Output:", check_if_path_exists_betweent_two_nodes(g,6,0))
        print("-" * 100)
        i += 1