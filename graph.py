# graph.py

class Graph:
    """Đồ thị vô hướng có trọng số đơn giản dùng danh sách kề."""

    def __init__(self):
        # adj: dict[đỉnh] = list[(đỉnh_kề, trọng_số)]
        self.adj = {}
        # edges: list các cạnh dạng (u, v, w)
        self.edges = []

    @property
    def vertices(self):
        """Trả về danh sách các đỉnh."""
        return list(self.adj.keys())

    def add_vertex(self, v):
        """Thêm đỉnh (nếu chưa tồn tại)."""
        if v not in self.adj:
            self.adj[v] = []

    def add_edge(self, u, v, w=1):
        """
        Thêm cạnh vô hướng (u, v) với trọng số w.
        Đồng thời cập nhật:
        - danh sách kề self.adj
        - danh sách cạnh self.edges
        """
        # Đảm bảo 2 đỉnh đã tồn tại trong adj
        self.add_vertex(u)
        self.add_vertex(v)

        # Thêm vào danh sách kề (vô hướng)
        self.adj[u].append((v, w))
        self.adj[v].append((u, w))

        # Lưu cạnh (u, v, w)
        # Để tránh trùng cạnh (v, u, w) thì ta luôn lưu theo thứ tự u < v (nếu là string)
        if u <= v:
            edge = (u, v, w)
        else:
            edge = (v, u, w)

        if edge not in self.edges:
            self.edges.append(edge)

    def neighbors(self, v):
        """Trả về danh sách các đỉnh kề của v (bỏ qua trọng số)."""
        return [to for (to, w) in self.adj.get(v, [])]
