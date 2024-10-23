def find_path_to_leaf(node, adj_list):
    if


def number_of_good_nodes(nodes, edges, required_good_nodes):

    adj_list=dict()
    for s,d in edges :
        if s in adj_list:
            adj_list[s].append(d)
        else:
            adj_list[s]=[d]
    find_path_to_leaf(1,adj_list)


if __name__ == '__main__':
    A = [0, 1, 0, 1, 1, 1]
    B = [[1, 2], [1, 5], [1, 6], [2, 3], [2, 4]]
    C = 1
    print(number_of_good_nodes(A,B,C))