from collections import deque


def minimum_buses(routes, src, dest):
    adj_list={}
    for i , stations in enumerate(routes):
        for station in stations:
            if station not in adj_list:
                adj_list[station]=[]
            adj_list[station].append(i)
    queue=deque()
    queue.append([src,0])
    visited_buses=set()
    while queue:
        station,buses_taken=queue.popleft()
        if station==dest:
            return buses_taken
        if station in adj_list:
            for bus in adj_list[station]:
                if bus not in visited_buses:
                    for s in routes[bus]:
                        queue.append([s,buses_taken+1])
                    visited_buses.add(bus)
    return -1


if __name__ == '__main__':
    routes = [[[2, 5, 7], [4, 6, 7]],
              [[1, 12], [4, 5, 9], [9, 19], [10, 12, 13]],
              [[1, 12], [10, 5, 9], [4, 19], [10, 12, 13]],
              [[1, 9, 7, 8], [3, 6, 7], [4, 9], [8, 2, 3, 7], [2, 4, 5]],
              [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
              ]
    src = [2, 9, 1, 1, 4]
    dest = [6, 12, 9, 5, 6]

    for i, bus in enumerate(routes):
        print(i + 1, ".\tBus Routes: ", bus, sep="")
        print("\tSource: ", src[i])
        print("\tDestination: ", dest[i])
        print("\n\tMinimum Buses Required: ", minimum_buses(bus, src[i], dest[i]))
        print("-" * 100)