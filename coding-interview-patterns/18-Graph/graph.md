# Graphs

## Introduction
A graph is a nonlinear data structure that represents connections between entities. In graph theory, entities are represented as vertices (or nodes), and the connections between them are expressed through edges.
#### Types of graphs
1. Undirected graph
2. Directed graph
3. Weighted graph
4. Cyclic graph
5. Acyclic graph

#### Graph representation
1. Adjacency list
2. Adjacency matrix
#### Graph traversal
1. Depth-first search (DFS)
2. Breadth-first search (BFS)
#### Graph algorithms
1. **Dijkstra’s algorithm:** It’s a variation of DFS and finds the shortest path between two nodes in a weighted graph.
2. **Bellman-Ford algorithm:** It’s a variation of BFS and finds the shortest paths in a weighted graph, even when negative edge weights are present.
3. **Floyd-Warshall algorithm:** It’s a variation of BFS and finds the shortest paths between all pairs of nodes in a weighted graph.
4. **Topological sorting:** It’s similar to DFS and orders nodes in a directed acyclic graph (DAG) to satisfy dependencies.
5. **Prim’s algorithm:** It finds the minimum spanning tree of a connected, undirected graph.
6. **Kruskal’s algorithm:** It also finds the minimum spanning tree of a connected, undirected graph.

## Example:
1. Find if a path exists in the graph
2. Find if a cycle exists in the graph
## Pattern:
**Relationships between elements:** There is a network of interconnected objects with some relationship between them; that is, the data can be represented as a graph.
## Real World problems:
1. Routing in computer networks
2. Flight route optimization
3. Epidemic spread modeling
4. Recommendation systems

## Practice Problems
### 1. Network Delay Time [Leetcode:Medium](https://leetcode.com/problems/network-delay-time/)
````
input:  A list of times (edges with travel times between nodes), the number of nodes n, and the starting node src
output: Find the time it takes for a signal to reach all nodes in the network, starting from src node
````
#### Steps : [Solution](../../Ostad/module-7:LinkedList/practice/reverse_linked_list.py)
1. create an adjacency list for src to dest with time required from the input
2. use a MinHeap to keep the minimum time edge at the top
3. push src with weight=0 and traverse using BFS 
4. for edge of the node push them in minHeap with new calculated weight
5. keep track of the visited node to check if all nodes can be reached from src 
6. keep an ans variable to for maximum delay time
#### Complexity
```
Time: 
The overall time complexity is dominated by the heap operations and processing neighbors:O((V+E)log⁡V)

Space:
Adjacency List: Takes O(E) space to store the edges.
Min-Heap: In the worst case, it stores O(V) nodes.
Visited Set: Stores O(V) nodes.
Overall Space Complexity: O(V + E).
```

### 2. Maze 

TODO 



















### 3. Graph Valid Tree [Leetcode:Premium](https://leetcode.com/problems/graph-valid-tree/description/)
````
input:  A list of undirected edges where each edge is list of 2 nodes
output: Find if the graph is a valid tree , meaning if it has no cycle and all nodes are reachable from other nodes
````
#### Steps : [Solution](../../Ostad/module-7:LinkedList/practice/reverse_linked_list.py)
1. If the number of edges is not equal to number of nodes - 1, return false.
2. Initialize adjacency list from the input
3. keep a set for visited nodes and stack to keep track of nodes and initialize both with the 0th node.
4. use DFS and stack to traverse all the nodes 
5. if any node is visited even after it is on the set , then return false, cause this means cycle.
6. if all nodes are visited and length of the set is the number of nodes , return true 
#### Complexity
```
Time: 
The overall time complexity is dominated by the heap operations and processing neighbors:O((V+E)log⁡V)

Space:
Adjacency List: Takes O(E) space to store the edges.
Min-Heap: In the worst case, it stores O(V) nodes.
Visited Set: Stores O(V) nodes.
Overall Space Complexity: O(V + E).
```
### 4. Bus Routes [Leetcode:Hard](https://leetcode.com/problems/bus-routes/description/)
````
input:  A list of list representing nodes of points in routes, a src and dest point
output: the number bus changes to reach destinantion
````
#### Steps : [Solution](bus_routes.py)
1. create an adjacency list that maps each station to the buses that travel trough station.
2. init a queue with src station and the bus count.
3. iterate the queue either till it is empty or the destination is reached.
4. visit connecting stations of the dequed nodes and enqueue connecting stations.
5. in every iteration, increase the bus count if a new bus is passing through the same station. 
6. return bus count.
#### Complexity
```
Time: 
O(R*S) , R =number of routes and S=number of stations
Space:
Adjacency List: Takes O(R*S) space to store the routes.
Queue: In the worst case, it stores O(R*S) nodes.
Visited Set: Stores O(S) nodes.
Overall Space Complexity: O(R*S).
```