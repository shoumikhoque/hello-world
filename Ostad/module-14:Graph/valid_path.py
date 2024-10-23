def has_valid_path(edges, source, destination):
    if source== destination:
        return True
    for edge  in edges:
        if edge[0]==source:
             return has_valid_path(edges,edge[1],destination)
    return False

if __name__ == '__main__':
    n = 3
    edges = [[0, 1], [1, 2], [2, 0]]
    source = 0
    destination = 2
    print(has_valid_path(edges,source,destination))