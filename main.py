from collections import defaultdict
import heapq

class Graph:
    def __init__(self):
        # adjacency list: u -> list of (v, w)
        self.adj = defaultdict(list)

    def add_edge(self, u, v, w=1):
        # vô hướng
        self.adj[u].append((v, w))
        self.adj[v].append((u, w))

    @property
    def vertices(self):
        return list(self.adj.keys())

    @property
    def edges(self):
        """Trả về list (u, v, w) mỗi cạnh chỉ xuất hiện 1 lần."""
        es = []
        seen = set()
        for u in self.adj:
            for v, w in self.adj[u]:
                if (v, u) not in seen:
                    es.append((u, v, w))
                    seen.add((u, v))
        return es


def  is_tree(graph: Graph):
    vertices = graph.vertices
    if not vertices:
        return False

    start = vertices[0]
    visited = set()

    def dfs(u, parent):
        visited.add(u)
        for v, _ in graph.adj[u]:
            if v == parent:
                continue
            if v in visited:
                # gặp lại đỉnh đã thăm -> có chu trình
                return False
            if not dfs(v, u):
                return False
        return True

    # không có chu trình?
    if not dfs(start, None):
        return False

    # tất cả đỉnh đều được thăm? (liên thông)
    if len(visited) != len(vertices):
        return False

    # (tuỳ chọn) kiểm tra |E| = |V| - 1
    if len(graph.edges) != len(vertices) - 1:
        return False

    return True


def spanning_tree_dfs(graph: Graph, start=None):
    if not graph.vertices:
        return []

    if start is None:
        start = graph.vertices[0]

    visited = set()
    tree_edges = []

    def dfs(u):
        visited.add(u)
        for v, w in graph.adj[u]:
            if v not in visited:
                tree_edges.append((u, v, w))  # cạnh thuộc spanning tree
                dfs(v)

    dfs(start)

    # Nếu đồ thị không liên thông thì spanning tree chỉ bao phủ thành phần chứa 'start'
    return tree_edges


def prim_mst(graph: Graph, start=None):
    if not graph.vertices:
        return []

    if start is None:
        start = graph.vertices[0]

    visited = set([start])
    mst_edges = []
    pq = []  # (w, u, v)

    # đưa các cạnh xuất phát từ start vào heap
    for v, w in graph.adj[start]:
        heapq.heappush(pq, (w, start, v))

    while pq and len(visited) < len(graph.vertices):
        w, u, v = heapq.heappop(pq)
        if v in visited:
            continue
        # chọn cạnh (u, v)
        visited.add(v)
        mst_edges.append((u, v, w))

        # thêm các cạnh mới từ v
        for x, wx in graph.adj[v]:
            if x not in visited:
                heapq.heappush(pq, (wx, v, x))

    return mst_edges

# Các cạnh của cây (trọng số bạn có thể đổi tuỳ ý)
g = Graph()
g.add_edge("A", "B", 9)
g.add_edge("A", "C", 3)
g.add_edge("A", "D", 6)
g.add_edge("C", "F", 6)
g.add_edge("A", "H", 8)
g.add_edge("H", "E", 29)

print("Đỉnh:", g.vertices)
print("Cạnh:", g.edges)

# Kiểm tra cây
print("Đồ thị là tree?", is_tree(g))

# # Tạo đồ thị giống hình (a)
# g = Graph()
# g.add_edge("A", "B", 9)
# g.add_edge("B", "D", 19)
# g.add_edge("A", "D", 6)
# g.add_edge("B", "E", 7)
# g.add_edge("E", "H", 29)
# g.add_edge("A", "H", 8)
# g.add_edge("A", "C", 3)
# g.add_edge("C", "F", 6)

# print("Đỉnh:", g.vertices)
# print("Cạnh:", g.edges)

# # Kiểm tra cây
# print("Đồ thị là tree?", is_tree(g))

# # Spanning tree bất kỳ
# st = spanning_tree_dfs(g, start="A")
# print("Spanning tree (DFS):", st)

# # Minimum Spanning Tree bằng Prim
# mst = prim_mst(g, start="A")
# print("MST (Prim):", mst, " -- tổng trọng số =", sum(w for _,_,w in mst))
