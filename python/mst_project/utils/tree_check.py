# mstlib/utils/tree_check.py
from typing import Set
from mstlib.graph import Graph, Vertex


def is_tree(graph: Graph) -> bool:
    vertices = graph.vertices()
    if not vertices:
        return True

    visited: Set[Vertex] = set()

    def dfs(u: Vertex, parent: Vertex | None) -> bool:
        visited.add(u)
        for v, _ in graph.neighbors(u):
            if v not in visited:
                if not dfs(v, u):
                    return False
            elif v != parent:
                # gặp lại đỉnh cũ mà không phải cha → chu trình
                return False
        return True

    # kiểm tra chu trình
    if not dfs(vertices[0], None):
        return False

    # kiểm tra liên thông
    return len(visited) == len(vertices)
