# run.py

from graph import Graph
from tree_utils import is_tree, spanning_tree_dfs, prim_mst


def main():
    # Tạo đồ thị giống hình (a)
    g = Graph()
    g.add_edge("A", "B", 9)
    g.add_edge("B", "D", 19)
    g.add_edge("A", "D", 6)
    g.add_edge("B", "E", 7)
    g.add_edge("E", "H", 29)
    g.add_edge("A", "H", 8)
    g.add_edge("A", "C", 3)
    g.add_edge("C", "F", 6)

    print("Đỉnh:", g.vertices)
    print("Cạnh:", g.edges)

    # Kiểm tra cây
    print("Đồ thị là tree?", is_tree(g))

    # Spanning tree bất kỳ bằng DFS
    st = spanning_tree_dfs(g, start="A")
    print("Spanning tree (DFS):", st)

    # Minimum Spanning Tree bằng Prim
    mst = prim_mst(g, start="A")
    total_weight = sum(w for _, _, w in mst)
    print("MST (Prim):", mst, " -- tổng trọng số =", total_weight)


if __name__ == "__main__":
    main()
