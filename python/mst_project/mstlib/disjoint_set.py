# mstlib/disjoint_set.py
from typing import Dict, Hashable

Vertex = Hashable

class DisjointSet:
    def __init__(self, items):
        self.parent: Dict[Vertex, Vertex] = {x: x for x in items}
        self.rank: Dict[Vertex, int] = {x: 0 for x in items}

    def find(self, x: Vertex) -> Vertex:
        while self.parent[x] != x:
            self.parent[x] = self.parent[self.parent[x]]  # path compression
            x = self.parent[x]
        return x

    def union(self, a: Vertex, b: Vertex) -> bool:
        ra, rb = self.find(a), self.find(b)
        if ra == rb:
            return False
        if self.rank[ra] < self.rank[rb]:
            ra, rb = rb, ra
        self.parent[rb] = ra
        if self.rank[ra] == self.rank[rb]:
            self.rank[ra] += 1
        return True
