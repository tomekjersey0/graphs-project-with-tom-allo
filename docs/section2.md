# Section 2: Design and Implementation

## Graph Representation

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

### Justification

An adjacency list was chosen over an adjacency matrix because:
- it is more **memory efficient** for sparse graphs (O(V + E))
- it allows efficient **iteration over neighbours**, which is essential for traversal algorithms such as BFS and DFS
- it aligns naturally with Python’s dictionary data structures

---

## Graph Operations

The graph supports several core operations:

### Adding Vertices and Edges

- `add_vertex(v)` inserts a vertex if it does not already exist  
- `add_edge(a, b)` creates a directed edge from A to B  

If either vertex does not exist, it is created automatically.

This ensures the graph remains consistent without requiring manual vertex management.

---

### Removing Vertices and Edges

- `remove_edge(a, b)` removes a specific edge if it exists  
- `remove_vertex(v)` removes a vertex and then calls a cleanup process  

When a vertex is removed, edges pointing to it may still exist.  
The `clean_graph()` method removes any such **stale edges**, ensuring the graph remains valid.

---

### Searching

- `find_vertex(v)` checks if a vertex exists  
- `find_edge(a, b)` checks if a specific edge exists  

Both operations are efficient, running in **O(1)** time due to dictionary lookup.

---

## Breadth-First Search (BFS)

BFS is implemented using a **queue (deque)** and explores the graph **level by level**.

### Algorithm Overview

1. Start from the initial vertex
2. Add it to a queue
3. Repeatedly:
   - remove a vertex from the queue
   - visit all unvisited neighbours
   - add those neighbours to the queue

### Implementation Details

- A dictionary is used to track visited vertices:
  - this preserves **insertion order**, allowing the traversal order to be returned directly
- The algorithm ensures each vertex is visited only once

### Properties

- Time complexity: **O(V + E)**
- Space complexity: **O(V)**
- Guarantees the **shortest path (in number of edges)** in unweighted graphs

---

## Depth-First Search (DFS)

DFS is implemented using **recursion**, which implicitly uses the call stack.

### Algorithm Overview

1. Start from the initial vertex
2. Visit a neighbour
3. Continue exploring deeper until no unvisited neighbours remain
4. Backtrack and continue with other paths

### Implementation Details

- A dictionary is used to track visited vertices
- Recursion replaces the need for an explicit stack

### Properties

- Time complexity: **O(V + E)**
- Space complexity: **O(V)**
- Explores full paths before moving to others
- Does **not guarantee shortest paths**

---

## Path Existence Checking

The method `path_exists_between(a, b)` determines whether a path exists between two vertices.

### Approach

- A modified BFS is used
- The search terminates early as soon as the target vertex is found

### Justification

BFS is appropriate because:
- it systematically explores all reachable vertices
- it ensures that if a path exists, it will be found efficiently

This avoids unnecessary traversal of the entire graph when a path is found early.

---

## Design Decisions

Several key design decisions were made during implementation:

### Adjacency List vs Adjacency Matrix

An adjacency list was chosen because:
- the graph is relatively **sparse**
- memory usage is significantly lower than an adjacency matrix
- traversal operations are more efficient

---

### Dictionary for Visited Tracking

A dictionary was used instead of a set to:
- preserve the **order of visitation**
- allow traversal order to be returned directly without additional structures

---

### Recursion for DFS

DFS was implemented recursively:
- simplifies the implementation
- leverages Python’s call stack instead of managing a manual stack

---

### Class-Based Structure

Although a non-object-oriented approach is possible, a class was used to:
- group related graph operations logically
- improve code organisation and readability
- encapsulate the graph structure and its behaviour

---

## Summary

The graph implementation uses an adjacency list to efficiently represent a directed, unweighted graph.

Core operations such as insertion, deletion, traversal, and path checking are implemented with appropriate data structures and algorithms, ensuring both correctness and efficiency.

The design prioritises:
- clarity
- efficiency for sparse graphs
- alignment with Python’s strengths

These choices provide a solid foundation for the graph operations used throughout the project.