# tree_utils.py

from graph import Graph   # import lớp Graph để dùng type hint (không bắt buộc)
import heapq


def is_tree(graph: Graph) -> bool:
    """
    Kiểm tra một đồ thị vô hướng có phải là cây (tree) hay không.

    Ý tưởng:
    - Dùng DFS:
        + Nếu trong quá trình duyệt gặp lại một đỉnh đã thăm mà không phải cha -> có chu trình -> không phải cây.
    - Sau DFS:
        + Nếu số đỉnh đã thăm != tổng số đỉnh -> không liên thông -> không phải cây.
    - (Tuỳ chọn) kiểm tra thêm |E| = |V| - 1 cho chắc chắn.
    """

    vertices = graph.vertices
    if not vertices:
        # Đồ thị rỗng -> không coi là cây
        return False

    start = vertices[0]  # chọn 1 đỉnh bất kỳ làm gốc DFS
    visited = set()

    def dfs(u, parent):
        """
        Duyệt sâu từ đỉnh u, 'parent' là đỉnh cha của u trong cây DFS.
        Nếu gặp lại đỉnh đã thăm (không phải cha) -> có chu trình.
        """
        visited.add(u)
        for v, _ in graph.adj[u]:
            if v == parent:
                # bỏ qua cạnh quay lại cha
                continue
            if v in visited:
                # gặp lại đỉnh đã thăm -> chu trình
                return False
            if not dfs(v, u):
                return False
        return True

    # 1) Kiểm tra không có chu trình
    if not dfs(start, None):
        return False

    # 2) Kiểm tra liên thông: tất cả đỉnh phải được thăm
    if len(visited) != len(vertices):
        return False

    # 3) (Tuỳ chọn) kiểm tra |E| = |V| - 1
    if len(graph.edges) != len(vertices) - 1:
        return False

    return True


def spanning_tree_dfs(graph: Graph, start=None):
    """
    Sinh ra một cây bao trùm (spanning tree) bất kỳ bằng DFS.

    Ý tưởng:
    - Chọn đỉnh start (hoặc lấy đỉnh đầu tiên).
    - Dùng DFS, mỗi lần đi sang đỉnh mới v từ u thì thêm cạnh (u, v, w) vào danh sách cây.
    - Các cạnh được chọn tạo thành một spanning tree nếu đồ thị ban đầu liên thông.
    """

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
                # cạnh (u, v) là cạnh của spanning tree
                tree_edges.append((u, v, w))
                dfs(v)

    dfs(start)

    # Nếu đồ thị không liên thông, spanning tree này chỉ bao phủ thành phần chứa 'start'
    return tree_edges


def prim_mst(graph: Graph, start=None):
    """
    Tìm Minimum Spanning Tree (MST) bằng thuật toán Prim.

    Ý tưởng:
    - Chọn đỉnh start, đưa các cạnh xuất phát từ start vào priority queue (heap) theo trọng số.
    - Mỗi bước:
        + Lấy cạnh nhẹ nhất (w, u, v) trong heap.
        + Nếu v đã được chọn rồi thì bỏ qua.
        + Ngược lại, thêm v vào tập visited và thêm cạnh (u, v, w) vào MST.
        + Đưa các cạnh từ v tới các đỉnh chưa được thăm vào heap.
    - Dừng khi đã chọn đủ |V| - 1 cạnh hoặc heap rỗng.
    """

    if not graph.vertices:
        return []

    if start is None:
        start = graph.vertices[0]

    visited = set([start])
    mst_edges = []
    pq = []  # heap: (w, u, v)

    # Đưa các cạnh xuất phát từ start vào heap
    for v, w in graph.adj[start]:
        heapq.heappush(pq, (w, start, v))

    # Lặp cho đến khi đã bao hết các đỉnh (hoặc hết cạnh)
    while pq and len(visited) < len(graph.vertices):
        w, u, v = heapq.heappop(pq)
        if v in visited:
            # nếu v đã thuộc MST rồi thì bỏ qua
            continue

        # Chọn cạnh (u, v) vào MST
        visited.add(v)
        mst_edges.append((u, v, w))

        # Thêm các cạnh mới từ v vào heap
        for x, wx in graph.adj[v]:
            if x not in visited:
                heapq.heappush(pq, (wx, v, x))

    return mst_edges
