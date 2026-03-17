# Graph

# Adjacency list implementation
class GRAPH_LIST:
    def __init__(self):
        self.graph: dict[str, set[str]]

    def add_vertex(self, v: str) -> None:
        self.graph.setdefault(v, set())

    def add_edge(self, a: str, b: str) -> None:
        self.graph.setdefault(a, set()).add(b)

    def remove_edge(self, a: str, b: str) -> None:
        if a in self.graph:
            self.graph[a].discard(b)
            if not self.graph[a]:
                del self.graph[a]

    def remove_vertex(self, v: str) -> None:
        if v in self.graph:
            del self.graph[v]

    def find_vertex(self, v: str) -> bool:
        return True if v in self.graph else False
    
    def find_edge(self, a: str, b: str) -> bool:
        neighbours: set[str] | None = self.graph.get(a)
        if neighbours is None:
            return False
        return b in neighbours

    def path_exists_between(self, a: str, b: str) -> bool:
        