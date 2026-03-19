from colorama import Fore, init
import search
import graph
from typing import Any

# makes sure that after each coloured print, it returns back to normal.
init(autoreset=True)

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

def t1():
    vs = "abcdefgh"
    es = "accafahdahdgfaef"
    g = build_graph(vs, es)
    
    return search.bfs(g,"a")

def t2():
    g = build_graph("", "")
    g.remove_vertex("a")

    return search.bfs(g, "a")

def t3():
    g = build_graph("abc", "abacbabccacb")
    g.remove_vertex("b")

    return search.bfs(g, "a")

def t4():
    g = graph.GRAPH_LIST()
    g.add_edge('a', 'b')

    return search.bfs(g, 'a')

def t5():
    g = graph.GRAPH_LIST()
    g.add_edge('a', 'a')

    return search.bfs(g, 'a')

def t6():
    g = build_graph("abc","abbcca")

    return search.bfs(g, 'a')
    

tests: list[Test] = [
    Test(t1,list("achdg")),
    Test(t2,[]),
    Test(t3,list("ac")),
    Test(t4,list("ab")),
    Test(t5,['a']),
    Test(t6,list("abc"))
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

results = run_tests(tests)

for r in results:
    result = r["result"]
    i = r["idx"]
    out = r["out"]
    t = r["test"]
    if result:
        print(f"{Fore.GREEN}Test {i+1} PASSED. Returns: {out}, expected: {t.exp}")
    else:
        print(f"{Fore.RED}Test {i+1} FAILED. Returns: {out}, expected: {t.exp}")
    