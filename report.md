# Graphs

A graph in computer science is a data structure made up of vertices and edges. It differs from a binary tree and linked list because each vertex can connect to multiple vertices with more than one edge.
   
 Graphs can either be directional or undirectional which one it is is decided whether there is an arrow on the edge or not, graphs can also be weighted which gives each edge a value showing the distance between vertex's

![graph](images/graph.png)
*insert image of weighted graph here, youve got it in one of your chat chats*

graphs are represented differently in different codes:
Python
    graph = {"A":["B","C","D"],"B":["A","E"],"C":["A","D"],"D":["A","C","F"],"E":["B","G"],"F":["D"],"G":["E"]}