# Graphs Project Report

## Section 1: Understanding Graphs

### What is a Graph?

A graph is a non-linear data structure consisting of vertices (nodes) and edges, where vertices represent entities and edges represent relationships between them.

#### Key Distinctions

##### Graphs vs. Trees
A tree is a restricted type of graph with a hierarchical structure, no cycles, and a single root. In contrast, a general graph has no such restrictions and may contain cycles and multiple paths between vertices.

##### Graphs vs. Linked Lists
A linked list is a linear structure where each vertex typically connects to a single next element, forming a simple chain rather than a network.

### Directed vs Undirected Graphs

Graphs can be classified based on whether their edges have direction.

#### Undirected Graphs

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

```
A → B
B → A
```


---

#### Directed Graphs

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
```
A → B
```

---

#### Key Differences

| Feature | Undirected Graph | Directed Graph |
|--------|----------------|----------------|
| Edge type | Unordered pair | Ordered pair |
| Direction | None | One-way |
| Symmetry | Yes | Not necessarily |
| Storage | Two entries per edge | One entry per edge |

---

#### Why This Matters

The choice between directed and undirected graphs affects:

- **Traversal**: In directed graphs, some vertices may not be reachable
- **Pathfinding**: Direction restricts valid paths
- **Representation**: Undirected graphs require storing edges twice in adjacency lists

### Weighted vs Unweighted Graphs

Graphs can also be classified based on whether edges carry additional values.

#### Unweighted Graphs

In an **unweighted graph**, edges do not store any additional information — they only represent whether a connection exists.

This means:
- all edges are treated equally
- traversal is based purely on structure

Unweighted graphs are typically used for:
- checking connectivity between vertices
- finding the shortest path in terms of **number of edges**

For example, in a road network where all roads are considered equal, the goal might be to minimise the number of steps rather than distance.

---

#### Weighted Graphs

In a **weighted graph**, each edge has an associated value (weight).

A weight represents a measurable quantity such as:
- distance
- time
- cost
- capacity

This means:
- edges are no longer equal
- traversal must consider edge weights when determining optimal paths

Weighted graphs are used in problems such as:
- finding the shortest route (minimum distance)
- minimising cost (e.g. cheapest flights)
- optimising resource usage

---

#### Key Differences

| Feature | Unweighted Graph | Weighted Graph |
|--------|----------------|----------------|
| Edge value | None | Numerical weight |
| Edge importance | All equal | Varies by weight |
| Shortest path meaning | Fewest edges | Minimum total weight |
| Algorithm used | BFS | Dijkstra’s algorithm (or similar) |

---

#### Why This Matters

The presence of weights changes how algorithms operate:

- In an **unweighted graph**, BFS can be used to find the shortest path efficiently  
- In a **weighted graph**, BFS is no longer sufficient, as it ignores weights  
- Instead, algorithms such as **Dijkstra’s algorithm** are required  

This distinction is important because it determines:
- which algorithms are valid
- how paths are evaluated
- how the graph must be stored and processed

### Python Implementations

Graphs can be represented in Python using an **adjacency list**, typically implemented with dictionaries.  
This is the representation used throughout the implementation in this project.

In this structure:
- each key represents a vertex
- the value represents its neighbouring vertices

This allows for efficient storage, especially for sparse graphs.

--- 

#### Undirected Graph

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

In this representation:
- edges are stored **in both directions** in the adjacency list representation
- if A is connected to B, then B is also connected to A

This reflects the definition of an **undirected graph**

<img src="images/undirected_graph_example.png" width="400"/>

This diagram shows that each connection appears in both directions (e.g. A ↔ B), matching how the adjacency list stores edges twice (A → B and B → A).

--- 

#### Directed Graph

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

Here:
- edges are stored **in one direction**
- for example, A → B exists, but B → A does not

This reflects the definition of a **directed graph**, where connections are one-way.

<img src="images/directed_graph_example.png" width="400"/>

This diagram shows that edges have direction (e.g. A → B but not B → A), matching the adjacency list where connections are only stored in one direction.

--- 

#### Weighted Graph

```
graph = {
    "A":{
        "B":2,
        "C":6,
        "D":3
    }
}
```

In this case:
- the value is a **dictionary instead of a list**
- each neighbour is mapped to a **weight**

This allows for storing additional information such as distance or cost.

<img src="images/weighted_graph_example.png" width="400"/>

This diagram shows weights labelled on each edge (e.g. A → B has weight 2), matching the adjacency list where each neighbour is mapped to a numerical value instead of just being listed.

---

#### Weighted and Directed Graph

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
This combines both concepts:
- edges have direction
- edges carry weights

<img src="images/weighted_and_directed_graph_example.png" width="400"/>

This diagram shows both direction and weight (e.g. A → B with weight 2), matching the adjacency list where edges are stored as key-value pairs and only exist in one direction.
---

### Adjacency List vs Adjacency Matrix

Graphs can be represented in multiple ways, the two most common being **adjacency lists** and **adjacency matrices**.

---

#### Adjacency List

An **adjacency list** stores, for each vertex, a list (or dictionary) of its neighbouring vertices.

In Python, this is typically implemented using a dictionary:
- keys represent vertices
- values represent their neighbours

This is the representation used throughout this project.

Example:
```
A → [B, C, D]
B → [A, E]
```

**Advantages:**
- Efficient for **sparse graphs** (few edges)
- Uses less memory (O(V + E))
- Fast to iterate over neighbours

**Disadvantages:**
- Slower to check if a specific edge exists
- Structure is slightly more complex than a matrix

---

#### Adjacency Matrix

An **adjacency matrix** is a 2D array where:
- rows represent starting vertices
- columns represent destination vertices

A value indicates whether an edge exists (or stores a weight).

Example:
```
    A B C D
A [ 0 1 1 1 ]
B [ 1 0 0 0 ]
C [ 1 0 0 1 ]
D [ 1 0 1 0 ]
```


<img src="images/table.png" width="400" height="300"/>

**Advantages:**
- Very fast edge lookup (O(1))
- Simple and easy to understand

**Disadvantages:**
- Uses more memory (O(V²))
- Inefficient for sparse graphs

---

#### Key Differences

| Feature | Adjacency List | Adjacency Matrix |
|--------|----------------|------------------|
| Storage | O(V + E) | O(V²) |
| Edge lookup | Slower | Fast (O(1)) |
| Memory use | Efficient | Expensive |
| Best for | Sparse graphs | Dense graphs |

---

#### Why This Matters

The choice of representation affects both performance and usability:

- **Adjacency lists** are better when the graph has relatively few edges  
- **Adjacency matrices** are better when fast edge lookup is required  

In this project, an adjacency list was chosen because:
- the graph is relatively sparse  
- efficient traversal (BFS/DFS) is required  
- it aligns naturally with Python dictionary structures  

### Real-World Applications of Graphs

Graphs are widely used to model real-world systems where relationships between entities are important.

---

#### Navigation and Road Networks

In navigation systems, graphs are used to represent road networks.

- **Vertices** represent locations (e.g. cities or intersections)
- **Edges** represent roads connecting them
- **Weights** can represent distance or travel time

This allows algorithms to find the shortest or fastest route between two points.

---

#### Social Networks

Graphs are used to model relationships between people.

- **Vertices** represent users
- **Edges** represent relationships (e.g. friendships or followers)

Directed graphs are often used for platforms like Twitter, where relationships are not always mutual.

---

#### Computer Networks

Graphs model how devices are connected in a network.

- **Vertices** represent devices (e.g. routers or computers)
- **Edges** represent communication links

This helps in routing data efficiently and detecting network failures.

---

#### Task Scheduling and Dependencies

Graphs are used to represent dependencies between tasks.

- **Vertices** represent tasks
- **Edges** represent dependencies (A must be completed before B)

These are typically **directed graphs**, and are used in:
- project planning
- build systems
- operating systems

---

#### Why Graphs Are Suitable

Graphs are useful because they:
- model relationships clearly
- allow efficient traversal and pathfinding
- can represent both simple and complex systems

This makes them a flexible and powerful data structure for many real-world problems.They also allow the application of standard algorithms (such as BFS, DFS, and shortest path algorithms), making them highly practical.

## Section 2: Design and Implementation

### Graph Representation

The graph in this project is implemented using an **adjacency list**, represented in Python as a dictionary of dictionaries:
```python
dict[str, dict[str, Any]]
```

In this structure:
- each key represents a **vertex**
- each value is another dictionary representing its **neighbouring vertices**

For example:
```
A → {B: None, C: None}
```


This indicates that vertex A has directed edges to B and C.

The graph is implemented as a **directed, unweighted graph**:
- edges have direction (A → B does not imply B → A)
- edge values are set to `None`, but the structure allows for future extension to **weighted graphs**

#### Justification

An adjacency list was chosen over an adjacency matrix because:
- it is more **memory efficient** for sparse graphs (O(V + E))
- it allows efficient **iteration over neighbours**, which is essential for traversal algorithms such as BFS and DFS
- it aligns naturally with Python’s dictionary data structures

---

### Graph Operations

The graph supports several core operations:

#### Adding Vertices and Edges

- `add_vertex(v)` inserts a vertex if it does not already exist  
- `add_edge(a, b)` creates a directed edge from A to B  

If either vertex does not exist, it is created automatically.

This ensures the graph remains consistent without requiring manual vertex management.

---

#### Removing Vertices and Edges

- `remove_edge(a, b)` removes a specific edge if it exists  
- `remove_vertex(v)` removes a vertex and then calls a cleanup process  

When a vertex is removed, edges pointing to it may still exist.  
The `clean_graph()` method removes any such **stale edges**, ensuring the graph remains valid.

---

#### Searching

- `find_vertex(v)` checks if a vertex exists  
- `find_edge(a, b)` checks if a specific edge exists  

Both operations are efficient, running in **O(1)** time due to dictionary lookup.

---

### Breadth-First Search (BFS)

BFS is implemented using a **queue (deque)** and explores the graph **level by level**.

#### Algorithm Overview

1. Start from the initial vertex
2. Add it to a queue
3. Repeatedly:
   - remove a vertex from the queue
   - visit all unvisited neighbours
   - add those neighbours to the queue

#### Implementation Details

- A dictionary is used to track visited vertices:
  - this preserves **insertion order**, allowing the traversal order to be returned directly
- The algorithm ensures each vertex is visited only once

#### Properties

- Time complexity: **O(V + E)**
- Space complexity: **O(V)**
- Guarantees the **shortest path (in number of edges)** in unweighted graphs

---

### Depth-First Search (DFS)

DFS is implemented using **recursion**, which implicitly uses the call stack.

#### Algorithm Overview

1. Start from the initial vertex
2. Visit a neighbour
3. Continue exploring deeper until no unvisited neighbours remain
4. Backtrack and continue with other paths

#### Implementation Details

- A dictionary is used to track visited vertices
- Recursion replaces the need for an explicit stack

#### Properties

- Time complexity: **O(V + E)**
- Space complexity: **O(V)**
- Explores full paths before moving to others
- Does **not guarantee shortest paths**

---

### Path Existence Checking

The method `path_exists_between(a, b)` determines whether a path exists between two vertices.

#### Approach

- A modified BFS is used
- The search terminates early as soon as the target vertex is found

#### Justification

BFS is appropriate because:
- it systematically explores all reachable vertices
- it ensures that if a path exists, it will be found efficiently

This avoids unnecessary traversal of the entire graph when a path is found early.

---

### Design Decisions

Several key design decisions were made during implementation:

#### Adjacency List vs Adjacency Matrix

An adjacency list was chosen because:
- the graph is relatively **sparse**
- memory usage is significantly lower than an adjacency matrix
- traversal operations are more efficient

---

#### Dictionary for Visited Tracking

A dictionary was used instead of a set to:
- preserve the **order of visitation**
- allow traversal order to be returned directly without additional structures

---

#### Recursion for DFS

DFS was implemented recursively:
- simplifies the implementation
- leverages Python’s call stack instead of managing a manual stack

---

#### Class-Based Structure

Although a non-object-oriented approach is possible, a class was used to:
- group related graph operations logically
- improve code organisation and readability
- encapsulate the graph structure and its behaviour

---

### Summary

The graph implementation uses an adjacency list to efficiently represent a directed, unweighted graph.

Core operations such as insertion, deletion, traversal, and path checking are implemented with appropriate data structures and algorithms, ensuring both correctness and efficiency.

The design prioritises:
- clarity
- efficiency for sparse graphs
- alignment with Python’s strengths

These choices provide a solid foundation for the graph operations used throughout the project.

## Section 3: Testing, Evaluation and Reflection

### Testing Strategy

A structured testing approach was used to validate both the correctness and robustness of the graph implementation.

The goal of testing was to ensure:
- correct traversal behaviour (BFS and DFS)
- correct handling of graph operations (adding/removing vertices and edges)
- robustness against edge cases (e.g. cycles, self-loops, empty graphs)
- correctness of path existence checking

Tests were designed to cover both **typical usage scenarios** and **edge cases**, ensuring the implementation behaves reliably under different conditions.

---

### Test Design

Test cases were grouped into categories to ensure all aspects of the system were validated.

#### Core Functionality

These tests verify that the main traversal algorithms work correctly on standard graphs.

- BFS traversal from a starting node  
- DFS traversal on a linear structure  

Example:
- `t1`: BFS traversal on a connected graph  
- `t9`: DFS traversal on a linear graph  

These confirm that the graph is stored correctly and that traversal visits all reachable vertices.

---

#### Structural Integrity

These tests ensure that the graph remains valid after modification operations.

- Removing a vertex and ensuring edges are cleaned up  
- Adding edges that implicitly create vertices  
- Removing non-existent edges safely  

Examples:
- `t3`: Removing a vertex and ensuring stale edges are removed  
- `t4`: Adding an edge where vertices do not yet exist  
- `t13`: Attempting to remove a non-existent edge  

These tests confirm that the graph maintains consistency after updates.

---

#### Edge Cases

These tests focus on scenarios that often cause logical errors in graph implementations.

- Empty graph  
- Self-loops  
- Cycles  
- Disconnected graphs  

Examples:
- `t2`: Empty graph handling  
- `t5`: Self-loop behaviour  
- `t6`, `t11`: Cycle handling  
- `t12`: Unreachable vertex detection  

These are important because:
- cycles can cause infinite loops if visited tracking is incorrect  
- self-loops test whether a node is revisited incorrectly  
- disconnected graphs ensure traversal does not include unreachable nodes  

---

#### Logical Correctness

These tests verify higher-level behaviour of the graph.

- Path existence between vertices  

Examples:
- `t7`: Path exists  
- `t8`: Path does not exist  

These confirm that the BFS-based path checking algorithm functions correctly.

---

### Test Results

All implemented test cases passed successfully.

Each test compared the **expected output** with the **actual output**, confirming that:
- traversal orders were correct
- graph operations behaved as intended
- edge cases were handled without errors

The use of automated tests ensured consistency and allowed rapid validation after changes.

An example screenshot of such test results is shown below:

![test result screenshot](images/test_result.png)
---

### BFS vs DFS Evaluation

The implementation demonstrates clear differences between BFS and DFS.

#### Breadth-First Search (BFS)

- Explores the graph level-by-level  
- Uses a queue (FIFO)  
- Guarantees shortest path in unweighted graphs  

In testing, BFS produced traversal orders that reflect increasing distance from the starting node.

---

#### Depth-First Search (DFS)

- Explores as deeply as possible before backtracking  
- Uses recursion (implicit stack)  
- Does not guarantee shortest path  

In tests such as `t10`, DFS explores one branch fully before moving to another, demonstrating its depth-first nature.

---

#### Comparison

| Feature | BFS | DFS |
|--------|-----|-----|
| Structure | Queue | Stack / recursion |
| Exploration | Level-by-level | Deep exploration |
| Shortest path | Yes (unweighted) | No |
| Use case | Shortest path, connectivity | Full exploration, cycle detection |

This comparison shows that both algorithms are suited to different types of problems.

---

### Evaluation of Representation

The graph uses an **adjacency list** representation.

#### Advantages

- Efficient memory usage: O(V + E)  
- Fast iteration over neighbours  
- Well-suited for sparse graphs  

#### Limitations

- Slower edge lookup compared to adjacency matrix  
- Slightly more complex structure  

Overall, the adjacency list was appropriate because:
- the graph is relatively sparse  
- traversal operations (BFS/DFS) are the primary focus  

---

### Complexity Analysis

The main operations have the following time complexities:

- Add vertex: O(1)  
- Add edge: O(1)  
- Remove edge: O(1)  
- Remove vertex: O(V + E)  
- BFS traversal: O(V + E)  
- DFS traversal: O(V + E)  
- Path existence check: O(V + E)  

This shows that the implementation scales efficiently with graph size.

---

### Limitations and Improvements

Although the implementation is functional, several improvements could be made:

- **Weighted graphs**: Currently, edge weights are not used. This could be extended to support algorithms such as Dijkstra’s algorithm.  
- **Undirected graph support**: The current implementation is directed only. Adding bidirectional edges would allow more flexibility.  
- **Iterative DFS**: An explicit stack-based DFS could be implemented to avoid recursion limits.  
- **Visualisation**: A graphical representation of the graph could improve usability and debugging.  

---

### Team Contribution

The project was completed as a group, however responsibilities were divided unevenly.

I was primarily responsible for the design and implementation of the graph system in Section 2, including the adjacency list structure, BFS and DFS algorithms, and additional operations such as vertex/edge management and path checking. I also designed and implemented all test cases used in this section, including edge cases such as cycles, self-loops, and disconnected graphs.

Tom initially contributed to Section 1 by drafting the theoretical explanation of graphs. This was later refined and expanded to improve clarity and accuracy.

Some collaboration took place when discussing overall structure and ensuring consistency between sections, but the majority of the technical implementation and testing was completed independently.

---

### Conclusion

The testing process demonstrates that the graph implementation is correct, robust, and capable of handling a wide range of scenarios.

Both BFS and DFS are implemented effectively and behave as expected, and the chosen adjacency list representation provides an efficient and suitable structure for the problem.

Overall, the system meets its objectives and provides a strong foundation for further extensions.