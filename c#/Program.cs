// Program.cs
using System;

namespace GraphTreeDemo
{
    internal class Program
    {
        static void Main(string[] args)
        {
            // Tạo đồ thị giống đoạn Python bạn đưa
            var g = new Graph();
            g.AddEdge("A", "B", 9);
            g.AddEdge("B", "D", 19);
            g.AddEdge("A", "D", 6);
            g.AddEdge("B", "E", 7);
            g.AddEdge("E", "H", 29);
            g.AddEdge("A", "H", 8);
            g.AddEdge("A", "C", 3);
            g.AddEdge("C", "F", 6);

            Console.WriteLine("Các đỉnh:");
            Console.WriteLine(string.Join(", ", g.Vertices));

            Console.WriteLine("\nCác cạnh:");
            foreach (var e in g.Edges)
            {
                Console.WriteLine($"({e.U}, {e.V}, w={e.W})");
            }

            bool isTree = TreeUtils.IsTree(g);
            Console.WriteLine($"\nĐồ thị là Tree? {isTree}");

            // 1. Duyệt DFS từ A
            Console.WriteLine("\nThứ tự duyệt DFS bắt đầu từ A:");
            var dfsOrder = TreeUtils.DfsOrder(g, "A");
            Console.WriteLine(string.Join(" -> ", dfsOrder));

            // 2. Spanning Tree bằng DFS
            Console.WriteLine("\nSpanning Tree bằng DFS (các cạnh được chọn theo thứ tự):");
            var stDfs = TreeUtils.SpanningTreeDfs(g, "A");
            int step = 1;
            foreach (var e in stDfs)
            {
                Console.WriteLine($"Bước {step}: chọn cạnh ({e.U}, {e.V}) với w = {e.W}");
                step++;
            }

            // 3. Minimum Spanning Tree bằng Prim từ A
            Console.WriteLine("\nMinimum Spanning Tree (Prim) bắt đầu từ A:");
            var mst = TreeUtils.PrimMst(g, "A");
            int totalWeight = 0;
            step = 1;

            foreach (var e in mst)
            {
                Console.WriteLine($"Bước {step}: chọn cạnh ({e.U}, {e.V}) với w = {e.W}");
                totalWeight += e.W;
                step++;
            }

            Console.WriteLine($"\nTổng trọng số MST = {totalWeight}");

            Console.WriteLine("\nNhấn Enter để thoát...");
            Console.ReadLine();
        }
    }
}
