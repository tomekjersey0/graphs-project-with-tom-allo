# Graphs

## What is a Graph?

A graph is a non-linear data structure consisting of vertices (representing individual data points or entities) and edges (the connections between them that represent relationships).

### Key Distinctions
### Graphs vs. Trees
Graphs differ from Trees or Linked Lists. Where a Tree is a strictly hierarchical structure with a single root and no cycles, a Graph is a more general network where any vertex can connect to any other, allowing for multiple paths, cycles, and even self-loops.

### Graphs vs. Linked Lists
While a Linked List is a linear sequence where each vertex point to exactly one successor, a graph is a nonlinear network where any vertex can connect to multiple others, forming complex paths and cycles. 

## Directed vs Undirected Graphs

Graphs can be classified based on whether their edges have direction.

### Undirected Graphs

In an **undirected graph**, edges have no direction.  
If there is an edge between A and B, the connection works both ways.

Formally, an edge is represented as an **unordered pair**:
(A, B) = (B, A)

This means:
- movement between vertices is symmetric
- relationships are mutual

Examples include:
- friendships in social networks
- physical connections like roads (when travel is possible both ways)

In an adjacency list, undirected edges are typically stored twice:

A -> B<br>
B -> A



---

### Directed Graphs

In a **directed graph (digraph)**, edges have a specific direction.

An edge from A to B does **not** imply an edge from B to A.

Formally, edges are **ordered pairs**:
(A, B) ≠ (B, A)

This means:
- relationships are not necessarily mutual
- traversal must follow edge direction

Examples include:
- social media followers (A follows B)
- web links (page A links to page B)
- task dependencies (A must happen before B)

In an adjacency list, edges are stored only in one direction:

A -> B


---

### Key Differences

| Feature | Undirected Graph | Directed Graph |
|--------|----------------|----------------|
| Edge type | Unordered pair | Ordered pair |
| Direction | None | One-way |
| Symmetry | Yes | Not necessarily |
| Storage | Two entries per edge | One entry per edge |

---

### Why This Matters

The choice between directed and undirected graphs affects:

- **Traversal**: In directed graphs, some vertices may not be reachable
- **Pathfinding**: Direction restricts valid paths
- **Representation**: Undirected graphs require storing edges twice in adjacency lists

## Weighted vs Unweighted Graphs

**Unweighted Graphs** have edges with no associated value—they simply show whether a connection exists or not. These are used for finding any path between two points or checking if vertices are connected. For example, checking if there is a route between City A and City B.

**Weighted Graphs** have edges with associated values (weights) representing distance, cost, time, or strength of connection. These are used for finding shortest paths, minimizing costs, and optimization problems. For example, finding the shortest distance route from City A to City B or the cheapest flight connection.

## Python Implementations

Below are Python code examples showing how to represent each type of graph using an adjacency list (dictionary):

Undirected graph in Python
```
graph = {
    "A":["B","C","D"],
    "B":["A","E"],
    "C":["A","D"],
    "D":["A","C","F"],
    "E":["B","G"],
    "F":["D"],
    "G":["E"]
}
```

Directed graph in python
```
graph = {
    "A":["B","C","D"],
    "B":["E"],
    "C":["D"],
    "D":["F"],
    "E":["G"],
    "F":[], 
    "G":[]
} 
```

Weighted graph in python
```
graph = {
    "A":{
        "B":2,
        "C":6,
        "D":3
    }
}
```

Weighted and directed graph in python
```
graph = {
    "A":{"B":2,"C":6,"D":3},
    "B":{"E":4},
    "C":{"D":1},
    "D":{"F":5},
    "E":{"G":3},
    "F":{},
    "G":{}
}
```

<img src="images/graph.png" width="400" height="275"/>


<img src="images/image.png" width="400" height="300"/>


## Adjacency list vs Adjacency matrix

Graphs are typically stored as objects or dictionaries known as **adjacency lists** they can also be stored as a 2D array or a list of lists. This implementation is known as an **adjacency matrix** with rows and columns representing verticies and edges. An example of an adjacency matrix for the undirected graph is shown below


<img src="images/table.png" width="400" height="300"/>



## Real-world applications
graphs in computer science have many uses. For example mapping road netowrks for navigation systems, storing social network data, resource allocation in operatnig systems and many others.

## traversal concepts
