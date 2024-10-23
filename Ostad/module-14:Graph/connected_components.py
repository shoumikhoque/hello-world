def dfs(node, adj_list, visited):
    visited[node] = True
    for neighbor in adj_list[node]:
        if not visited[neighbor]:
            dfs(neighbor, adj_list, visited)

def total_connected_components(adj_list, num_nodes):
    visited = [False] * num_nodes
    count = 0

    for node in range(num_nodes):
        if not visited[node]:
            dfs(node, adj_list, visited)
            count += 1  # Increment count for each new connected component
    return count

if __name__ == '__main__':
    nodes = 4

    adj_list = {
        0: [1],
        1: [0, 2],
        2: [1],
        3: [4],
        4: [3]
    }
    print(total_connected_components(adj_list,nodes))