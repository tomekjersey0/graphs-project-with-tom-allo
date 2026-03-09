# Project Brief: Graphs

Group [2 people] / Individual project

---

# Section 1: Understanding and Explanation of Graphs

## Core expectation

- What a graph is (vertices/nodes and edges)
- Directed vs undirected graphs
- Weighted vs unweighted graphs
- Adjacency list vs adjacency matrix
- Real-world applications (navigation, social networks, networks, scheduling)
- Traversal concepts (BFS/DFS overview)

---

## Rubric descriptors

### Excellent (8–10)

- Gives a clear, accurate and detailed explanation of graphs using correct terminology (vertex/node, edge, directed/undirected, weighted/unweighted).
- Correctly explains at least two representations (e.g., adjacency list and adjacency matrix), including strengths/limitations.
- Includes relevant real-world examples and explains why graphs fit those problems.
- Explains BFS/DFS conceptually and distinguishes them appropriately (e.g., shortest path in unweighted graph vs depth exploration).

### Secure (6–7)

- Gives a mostly accurate explanation of graphs and key terminology.
- Correctly describes directed/undirected and weighted/unweighted graphs.
- Identifies at least one graph representation and one or more applications.
- Shows some understanding of BFS/DFS, though explanations may lack depth.

### Developing (4–5)

- Basic explanation of graphs is present but may be incomplete or vague.
- Some terminology is used correctly, but there may be confusion (e.g., edges vs vertices).
- Mentions examples/applications but with limited explanation.
- BFS/DFS may be named but not clearly explained.

### Beginning (2–3)

- Limited understanding of graphs.
- Definitions are partially correct or inconsistent.
- Very little use of correct technical vocabulary.
- Minimal or unclear discussion of graph types or uses.

### Limited (0–1)

- Very little relevant content.
- Major misunderstandings of what a graph is.
- No meaningful explanation of graph concepts.

---

# Section 2: Graph Implementation and Algorithms

## Core expectation

- Create a graph representation (dictionary adjacency list or adjacency matrix)
- Implement BFS and DFS correctly

---

## Rubric descriptors

### Excellent (8–10)

- Implements a graph correctly (clear representation, sensible structure).
- Correctly implements both BFS and DFS (iterative and/or recursive, without using OOP).
- Demonstrates traversal output clearly and correctly from a chosen start node.
- Implements numerous additional graph operations, such as:
  - add vertex
  - add edge
  - remove edge
  - remove vertex
  - search for a vertex/edge
  - check connectivity/path existence
- Code is readable and logically structured (good naming, comments, sensible decomposition into functions).
- Handles edge cases reasonably (e.g., duplicate vertices, missing nodes, invalid removals).

### Secure (6–7)

- Implements a graph representation correctly.
- Implements traversal algorithms (BFS or DFS).
- Can demonstrate traversal from a given start node.
- Includes some additional functionality (e.g., add/remove edge or vertex).
- Code mostly works and is understandable.

### Developing (4–5)

- Graph representation is present but limited or inconsistent.
- Attempts BFS/DFS but may have logic errors or only partial success.
- Limited additional operations.
- Code may work only for a narrow test case.
- Some structure/comments present but clarity is inconsistent.

### Beginning (2–3)

- Partial implementation only (e.g., graph stored but traversal not working).
- Major errors in BFS/DFS logic (queue/stack confusion, repeated nodes, etc.).
- Very limited functionality beyond storing data.
- Code difficult to follow.

### Limited (0–1)

- Little or no working graph implementation.
- No meaningful traversal algorithm implemented.

---

# Section 3: Testing, Evaluation and Communication

Possible titles:

- Testing and Evaluation
- Demonstration and Analysis
- Validation, Reflection and Teamwork

## Areas you could include

- Test cases
- Expected vs actual outputs
- Screenshots or sample outputs
- Reflection on bugs/challenges and how they fixed them
- Comparison of BFS vs DFS behaviour
- Strengths and limitations of their implementation
- Clear explanation of each group member’s contribution
- Big-O for graph operations

---

## Rubric descriptors

### Excellent (8–10)

- Thorough testing with multiple test cases, including edge cases (e.g., missing vertex, disconnected graph, repeated edge).
- Clearly shows expected vs actual outcomes and explains results.
- Gives a thoughtful comparison of BFS and DFS (e.g., order differences, use cases).
- Evaluates graph representation choice (adjacency list vs matrix) and algorithm suitability.
- Clear communication/presentation of the project, with evidence of both group members contributing meaningfully.
- Reflection identifies improvements/extensions (e.g., weighted paths, Dijkstra’s algorithm, visualisation).
- Clear discussion around Big-O for different operations.

### Secure (6–7)

- Good testing with more than one example.
- Demonstrates that the code works and explains most outputs.
- Some evaluation of BFS/DFS or implementation choices.
- Group contribution is mostly clear.
- Includes at least one meaningful improvement idea.

### Developing (4–5)

- Basic testing shown, but limited range of cases.
- Some outputs shown, with limited explanation.
- Minimal evaluation or reflection.
- Group roles may be unclear or unevenly evidenced.

### Beginning (2–3)

- Very limited testing (e.g., only one successful run).
- Little explanation of whether the code works correctly.
- Reflection/evaluation is superficial.
- Weak evidence of collaboration.

### Limited (0–1)

- No meaningful testing or evaluation shown.
- No reflection or communication of results.

---

# Knowledge

A graph is a data structure consisting of nodes (vertices) and pointers (edges). It differs from a linked list and binary tree because each vertex can have more than one or two edges and point to any vertex in the data structure.

Edges can point in one direction (directed graph) or without specifying a direction (undirected graph). Graphs can also be weighted, meaning each edge has a value representing a relationship such as distance between vertices.

Vertices are often called **nodes**, and edges may also be called **links** or **pointers**.

---

## Example Graph Representation (Python)

### Undirected Graph

```python
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

### Pseudocode Representation

```
Edges {
(A,B), (A,C), (A,D),
(B,A), (B,E),
(C,A), (C,D),
(D,A), (D,C), (D,F),
(E,B), (E,G),
(F,D),
(G,E)
}
```

### Directed Graph

```python
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

---

## Weighted Graph Example

```python
graph = {
"A": {"B":2, "C":6, "D":3}
}
```

This means:

- Edge A → B has cost 2
- Edge A → C has cost 6
- Edge A → D has cost 3

Edge weights can represent:

- distance
- time
- bandwidth
- cost

Weighted graphs are required for algorithms such as **Dijkstra’s shortest path algorithm**.

---

## Adjacency Matrix

Graphs can also be stored using an array (list of lists).

Rows and columns represent vertices, and a `1` indicates an edge exists between them.

Example concept:

```
    A B C D
A [ 0 1 1 1 ]
B [ 1 0 0 0 ]
C [ 1 0 0 1 ]
D [ 1 0 1 0 ]
```

---

# Applications of Graphs

Graphs have many uses in computer science, including:

- navigation systems and road networks
- social networks
- resource allocation in operating systems
- molecular structure modelling
- scheduling and dependency graphs

---

# Abstraction

Graphs and trees are closely related. A **binary tree is a special type of graph**.

Graph data may look visually different but still represent the same relationships. What matters is which vertices are connected, not how the graph is drawn.

A classic example of abstraction is the **London Underground map**, which does not represent geographic distances but only connectivity between stations.

---

## Why Use Abstraction?

Abstraction simplifies complex problems by focusing only on essential information.

Benefits include:

- easier understanding for humans
- clearer communication of data
- ability to recognise similarities between different problems

Computers themselves do not require visual abstraction — it mainly helps human reasoning.

---

# Depth-First Search (DFS) Example

```python
GRAPH = {
"A": ["B", "D", "E"],
"B": ["A", "D", "C"],
"C": ["B", "G"],
"D": ["A", "B", "E", "F"],
"E": ["A", "D"],
"F": ["D"],
"G": ["C"]
}

def dfs_iterative(graph, start_vertex):
    stack = [start_vertex]
    visited = []

    while len(stack) > 0:
        current_node = stack.pop()

        if current_node not in visited:
            visited.append(current_node)

            # Push neighbours in reverse order
            for neighbour in reversed(graph[current_node]):
                if neighbour not in visited:
                    stack.append(neighbour)

    return visited

visited_nodes = dfs_iterative(GRAPH, "A")
print("List of nodes visited:", visited_nodes)
```
