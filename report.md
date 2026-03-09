# Graphs

A graph in computer science is a data structure made up of vertices and edges. It differs from a binary tree and linked list because each vertex can connect to multiple vertices with more than one edge.
   
 Graphs can either be directional or undirectional which one it is is decided whether there is an arrow on the edge or not, graphs can also be weighted which gives each edge a value showing the distance between vertex's

![graph](images/graph.png)
*insert image of weighted graph here, youve got it in one of your chat chats*

Example of graphs written in python when undirected, directed and when its weighted

Undirected graph in Python
    graph = {"A":["B","C","D"],"B":["A","E"],"C":["A","D"],"D":["A","C","F"],"E":["B","G"],"F":["D"],"G":["E"]}

Directed graph in python
    graph = {"A":["B","C","D"],"B":["E"],"C":["D"],"D":["F"],"E":["G"],"F":[], "G":[]} 

Weighted graph in python
    graph = {"A":{"B":2,"C":6,"D":3}