# mstlib/algorithms/prim.py
import heapq
from dataclasses import dataclass
from typing import List, Optional, Set, Tuple

from mstlib.graph import Graph, Edge, Vertex


@dataclass
class PrimResult:
    edges: List[Edge]
    total_weight: float


class PrimAlgorithm:
    def run(self, graph: Graph, start: Optional[Vertex] = None, verbose: bool = False) -> PrimResult:
        vs = graph.vertices()
        if not vs:
            return PrimResult([], 0.0)

        if start is None:
            start = vs[0]

        visited: Set[Vertex] = {start}
        mst: List[Edge] = []
        total = 0.0
        pq: List[Tuple[float, Vertex, Vertex]] = []

        for v, w in graph.neighbors(start):
            heapq.heappush(pq, (w, start, v))

        if verbose:
            print(f"[Prim] start={start}")

        while pq and len(visited) < len(vs):
            w, u, v = heapq.heappop(pq)
            if v in visited:
                continue

            visited.add(v)
            mst.append(Edge(u, v, w))
            total += w

            if verbose:
                print(f"  choose ({u}-{v}) w={w}, visited={visited}")

            for x, wx in graph.neighbors(v):
                if x not in visited:
                    heapq.heappush(pq, (wx, v, x))

        return PrimResult(mst, total)
