# mstlib/algorithms/kruskal.py
from dataclasses import dataclass
from typing import List

from mstlib.graph import Graph, Edge
from mstlib.disjoint_set import DisjointSet


@dataclass
class KruskalResult:
    edges: List[Edge]
    total_weight: float


class KruskalAlgorithm:
    def run(self, graph: Graph, verbose: bool = False) -> KruskalResult:
        vs = graph.vertices()
        if not vs:
            return KruskalResult([], 0.0)

        dsu = DisjointSet(vs)
        mst: List[Edge] = []
        total = 0.0

        edges = sorted(graph.edges(), key=lambda e: e.w)

        if verbose:
            print("[Kruskal] edges sorted:", [(e.u, e.v, e.w) for e in edges])

        for e in edges:
            if dsu.union(e.u, e.v):
                mst.append(e)
                total += e.w
                if verbose:
                    print(f"  add ({e.u}-{e.v}) w={e.w}")

        return KruskalResult(mst, total)
