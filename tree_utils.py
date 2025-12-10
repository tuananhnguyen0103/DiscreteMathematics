# tree_utils.py

from collections import deque

def is_connected(graph):
    """
    Kiểm tra đồ thị có liên thông không:
    - Dùng BFS/DFS bắt đầu từ 1 đỉnh bất kỳ.
    - Nếu số đỉnh đã thăm == tổng số đỉnh -> liên thông.
    """
    vertices = graph.vertices
    if not vertices:
        return False  # đồ thị rỗng coi như không phải liên thông

    start = vertices[0]
    visited = set()
    queue = deque([start])

    while queue:
        u = queue.popleft()
        if u in visited:
            continue
        visited.add(u)
        for v in graph.neighbors(u):
            if v not in visited:
                queue.append(v)

    return len(visited) == len(vertices)


def is_tree(graph):
    """
    Tree (cây) với đồ thị vô hướng:
    - Liên thông
    - Không có chu trình
    - Tương đương: số cạnh = số đỉnh - 1 và liên thông
    """
    n = len(graph.vertices)
    m = len(graph.edges)

    # Điều kiện cần cho tree
    if m != n - 1:
        return False

    # Kiểm tra liên thông
    if not is_connected(graph):
        return False

    # Nếu m = n-1 và liên thông thì đảm bảo không có chu trình
    return True
