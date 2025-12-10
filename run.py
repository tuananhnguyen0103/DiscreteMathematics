# main.py

from graph import Graph
from tree_utils import is_tree

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


if __name__ == "__main__":
    main()
