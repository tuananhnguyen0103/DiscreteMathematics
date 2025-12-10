# graph.py
from collections import defaultdict

class Graph:
    """
    Đồ thị vô hướng có trọng số, cài đặt bằng danh sách kề (adjacency list).
    adj: dict[u] = list[(v, w)]
    """

    def __init__(self):
        # adjacency list: u -> list of (v, w)
        self.adj = defaultdict(list)

    def add_edge(self, u, v, w=1):
        """
        Thêm cạnh vô hướng (u, v) với trọng số w.
        Vì là vô hướng nên phải thêm cho cả u và v.
        """
        self.adj[u].append((v, w))
        self.adj[v].append((u, w))

    @property
    def vertices(self):
        """
        Trả về danh sách các đỉnh trong đồ thị.
        (các key của dict adj)
        """
        return list(self.adj.keys())

    @property
    def edges(self):
        """
        Trả về list các cạnh (u, v, w) sao cho mỗi cạnh chỉ xuất hiện 1 lần.
        Dùng set 'seen' để tránh đếm (u, v) và (v, u) thành 2 cạnh khác nhau.
        """
        es = []
        seen = set()
        for u in self.adj:
            for v, w in self.adj[u]:
                if (v, u) not in seen:
                    es.append((u, v, w))
                    seen.add((u, v))
        return es
