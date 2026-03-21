from colorama import init
import search
import graph
from typing import Any

class Test:
    def __init__(self, test, expected_output):
        self.test = test
        self.exp = expected_output

    def run(self) -> tuple[Any, bool]:
        out = self.test()
        return out == self.exp, out

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

# Basic case
def t1():
    g = build_graph("abcdefgh", "accafahdahdgfaef")
    
    return search.bfs(g,"a")

# Empty removal
def t2():
    g = build_graph("", "")
    g.remove_vertex("a")

    return search.bfs(g, "a")

# Removed vertex ignored in edge list
def t3():
    g = build_graph("abc", "abacbabccacb")
    g.remove_vertex("b")

    return search.bfs(g, "a")

# Vertex created on add_edge
def t4():
    g = graph.GRAPH_LIST()
    g.add_edge('a', 'b')

    return search.bfs(g, 'a')

# Self-loop
def t5():
    g = graph.GRAPH_LIST()
    g.add_edge('a', 'a')

    return search.bfs(g, 'a')

# Cycle
def t6():
    g = build_graph("abc","abbcca")

    return search.bfs(g, 'a')

# Path exists
def t7():
    g = build_graph("abcdefg","abbccdafagefedda")

    return g.path_exists_between('a','d')

# Path doesn't exists
def t8():
    g = build_graph("abch","ab")

    return g.path_exists_between('a','h')

# DFS: Linear path
def t9():
    # a -> b -> c -> d
    g = build_graph("abcd", "abbccd")
    return search.dfs(g, "a")

# DFS: Branching (Deep Dive)
def t10():
    # a connects to b and c. b connects to d.
    # DFS should go a -> b -> d -> c (completely finishing b's branch first)
    g = build_graph("abcd", "abacbd")
    return search.dfs(g, "a")

# DFS: Cycle handling
def t11():
    g = build_graph("abc", "abbcca")
    return search.dfs(g, "a")

# DFS: Unreachable vertex
def t12():
    g = build_graph("abc", "ab") # c is isolated
    return "c" in search.dfs(g, "a")
    
# Remove non-existant edge
def t13():
    g = build_graph("abc", "ab")
    g.remove_edge("b","c")
    return search.bfs(g,"a")

tests: list[Test] = [
    Test(t1,list("achdg")),
    Test(t2,[]),
    Test(t3,list("ac")),
    Test(t4,list("ab")),
    Test(t5,['a']),
    Test(t6,list("abc")),
    Test(t7,True),
    Test(t8,False),
    Test(t9, list("abcd")),
    Test(t10, list("abdc")),
    Test(t11, list("abc")),
    Test(t12, False),
    Test(t13, list("ab"))
]

def run_tests(tests: list[Test]):
    results = []
    for i, t in enumerate(tests):
        result, out = t.run()

        results.append({
            "idx":i,
            "result":result,
            "out":out,
            "test":t
        })
    
    return results