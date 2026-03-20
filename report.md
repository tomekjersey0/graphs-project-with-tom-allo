# Graphs

## What is a Graph?

A graph is a data structure consisting of vertices (or nodes), which are individual data points or entities, and edges, which are connections between vertices that represent relationships.

Graphs differ from binary trees and linked lists because each vertex can connect to multiple other vertices with multiple edges between them, creating more complex relationships.

## Directed vs Undirected Graphs

**Undirected Graphs** have edges with no direction—a connection between A and B means you can travel both ways. The edges are shown as plain lines. Undirected graphs are used in social networks (friendships), road networks where you can travel in both directions, and collaborations. For example, if A is friends with B, then B is friends with A.


**Directed Graphs** have edges with direction, shown as arrows. An edge from A to B does not necessarily mean there's an edge from B to A. Directed graphs are used in social networks (followers), task dependencies, and web page links. For example, A can follow B on Twitter, but B doesn't necessarily follow A back.

## Weighted vs Unweighted Graphs

**Unweighted Graphs** have edges with no associated value—they simply show whether a connection exists or not. These are used for finding any path between two points or checking if nodes are connected. For example, checking if there is a route between City A and City B.

**Weighted Graphs** have edges with associated values (weights) representing distance, cost, time, or strength of connection. These are used for finding shortest paths, minimizing costs, and optimization problems. For example, finding the shortest distance route from City A to City B or the cheapest flight connection.

## Python Implementations

Below are Python code examples showing how to represent each type of graph using an adjacency list (dictionary):

Undirected graph in Python
```
graph = {"A":["B","C","D"],"B":["A","E"],"C":["A","D"],"D":["A","C","F"],"E":["B","G"],"F":["D"],"G":["E"]}
```

Directed graph in python
```
graph = {"A":["B","C","D"],"B":["E"],"C":["D"],"D":["F"],"E":["G"],"F":[], "G":[]} 
```

Weighted graph in python
```
graph = {"A":{"B":2,"C":6,"D":3}}
```

Weighted and directed graph in python
```
graph = {"A":{"B":2,"C":6,"D":3},"B":{"E":4},"C":{"D":1},"D":{"F":5},"E":{"G":3},"F":{},"G":{}}
```

<img src="images/graph.png" width="400" height="275"/>


<img src="images/image.png" width="400" height="300"/>


## Adjacency list vs Adjacency matrix

Graphs are typically stored as objects or dictionaries known as **adjacency lists** they can also be stored as a 2D array or a list of lists. This implementation is known as an **adjacency matrix** with rows and columns representing verticies and edges. An example of an adjacency matrix for the undirected graph is shown below


<img src="images/table.png" width="400" height="300"/>



## Real-world applications
graphs in computer science have many uses. For example mapping road netowrks for navigation systems, storing social network data, resource allocation in operatnig systems and many others.

## traversal concepts
