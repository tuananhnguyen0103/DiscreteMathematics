# examples/run_demo.py
from mstlib.graph import Graph
from mstlib.algorithms.prim import PrimAlgorithm
from mstlib.algorithms.kruskal import KruskalAlgorithm
import sys
from pathlib import Path

# thêm thư mục gốc project vào PYTHONPATH
ROOT = Path(__file__).resolve().parents[1]
sys.path.append(str(ROOT))

def build_graph() -> Graph:
    g = Graph()
    g.add_edge("A", "B", 9)
    g.add_edge("B", "D", 19)
    g.add_edge("A", "D", 6)
    g.add_edge("B", "E", 7)
    g.add_edge("E", "H", 29)
    g.add_edge("A", "H", 8)
    g.add_edge("A", "C", 3)
    g.add_edge("C", "F", 6)
    return g

def main():
    g = build_graph()

    prim = PrimAlgorithm().run(g, start="A", verbose=True)
    print("Prim MST:", [(e.u, e.v, e.w) for e in prim.edges], "total=", prim.total_weight)

    kruskal = KruskalAlgorithm().run(g, verbose=True)
    print("Kruskal MST:", [(e.u, e.v, e.w) for e in kruskal.edges], "total=", kruskal.total_weight)

if __name__ == "__main__":
    main()
