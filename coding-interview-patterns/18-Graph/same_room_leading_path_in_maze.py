from collections import defaultdict


def number_of_cyclic_paths(n, corridors):
    neighbours=defaultdict(set)
    cycles=0
    for room1,room2 in corridors:
        neighbours[room1].add(room2)
        neighbours[room2].add(room1)
        cycles+=len(neighbours[room1].intersection(neighbours[room2]))
    return cycles

if __name__ == '__main__':
    n=5
    corridors=[[1,2],[5,2],[4,1],[2,4],[3,1],[3,4],[1,5]]
    print(number_of_cyclic_paths(n,corridors))