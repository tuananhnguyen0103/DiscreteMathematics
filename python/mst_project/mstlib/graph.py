# mstlib/graph.py
from __future__ import annotations
from dataclasses import dataclass
from collections import defaultdict
from typing import Dict, Hashable, Iterable, List, Tuple

Vertex = Hashable


@dataclass(frozen=True)
class Edge:
    u: Vertex
    v: Vertex
    w: float = 1.0


class Graph:
    """Đồ thị vô hướng có trọng số - adjacency list."""

    def __init__(self) -> None:
        self._adj: Dict[Vertex, List[Tuple[Vertex, float]]] = defaultdict(list)

    @property
    def adj(self) -> Dict[Vertex, List[Tuple[Vertex, float]]]:
        return self._adj

    def add_edge(self, u: Vertex, v: Vertex, w: float = 1.0) -> None:
        self._adj[u].append((v, w))
        self._adj[v].append((u, w))

    def vertices(self) -> List[Vertex]:
        return list(self._adj.keys())

    def edges(self) -> List[Edge]:
        """Mỗi cạnh chỉ xuất hiện 1 lần."""
        seen = set()
        out: List[Edge] = []
        for u in self._adj:
            for v, w in self._adj[u]:
                if (v, u) not in seen:
                    out.append(Edge(u, v, w))
                    seen.add((u, v))
        return out

    def neighbors(self, u: Vertex) -> List[Tuple[Vertex, float]]:
        return self._adj.get(u, [])

