import search
import graph

g = graph.GRAPH_LIST()
g.add_vertex("a")
g.add_vertex("b")
g.add_vertex("c")
g.add_vertex("d")
g.add_vertex("e")
g.add_vertex("f")
g.add_vertex("g")
g.add_vertex("h")
g.add_edge("a","c")
g.add_edge("c","a")
g.add_edge("f","a")
g.add_edge("h","d")
g.add_edge("a","h")
g.add_edge("d","g")
g.add_edge("f","a")
g.add_edge("e","f")

ret = search.bfs(g,"a")
print(ret)