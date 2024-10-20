import heapq
from collections import defaultdict

def find_network_delay_time(times, n, k):
    adj_list=defaultdict(list)
    for src, dst,time in times:
        adj_list[src].append((dst,time))
    minHeap=[(0,k)]
    visited=set()
    ans=0
    while minHeap:
        time,node=heapq.heappop(minHeap)
        if node in visited:
            continue
        visited.add((node))
        ans=max(ans,time)
        neighbours=adj_list[node]
        for neighbour_node,neighbour_time in neighbours:
            if neighbour_node not in visited:
                heapq.heappush(minHeap,(time+neighbour_time,neighbour_node))
    return ans if len(visited)==n else -1

if __name__ == '__main__':
    times = [[1,2,1]]
    n = 2
    k = 2
    print(find_network_delay_time(times,n,k))