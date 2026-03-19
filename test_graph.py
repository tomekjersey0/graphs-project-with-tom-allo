import search
import graph
from typing import Any

class Test:
    def __init__(self, test, expected_output):
        self.test = test
        self.exp = expected_output

    def run(self) -> tuple[Any, bool]:
        out = self.test()
        return (out == self.exp, out)

def build_graph(vertices: str, edges: str) -> graph.GRAPH_LIST:
    vs = vertices
    vs_d = set(list(vs))
    es = list(edges)
    
    g = graph.GRAPH_LIST()
    for v in vs:
        g.add_vertex(v)

    if len(es) % 2 == 1:
        es.pop()
    
    for i in range(0,len(es),2):
        e = es[i]
        if e in vs_d and es[i+1] in vs_d:
            g.add_edge(e, es[i+1])
    
    return g

def t1():
    vs = "abcdefgh"
    es = "accafahdahdgfaef"
    g = build_graph(vs, es)
    
    return search.bfs(g,"a")

print(t1())

        

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

g2: graph.GRAPH_LIST = build_graph("askflahslgjkashgkljashgasj", "jkfabababababbababaabbahadskjghsdajkghsdkgjgkjhsdgjkldhlgkjsdhg")
print(search.bfs(g2,"a"))

ret = search.bfs(g,"a")
print(ret)
