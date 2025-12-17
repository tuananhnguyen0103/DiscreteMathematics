using System;
using Prim.Algorithms;
using Prim.Graph;

public class Program
{
    public static void Main()
    {
        var g = new Graph();

        // Demo giống ví dụ bạn hay dùng
        g.AddEdge("A", "B", 9);
        g.AddEdge("B", "D", 19);
        g.AddEdge("A", "D", 6);
        g.AddEdge("B", "E", 7);
        g.AddEdge("E", "H", 29);
        g.AddEdge("A", "H", 8);
        g.AddEdge("A", "C", 3);
        g.AddEdge("C", "F", 6);

        Console.WriteLine("Graph edges:");

        foreach (var e in g.Adj["A"])
        {
            Console.WriteLine($"A -> {e.To} (w={e.Weight})");
        }



        //var dfsOrder = DFS.Dfs(g, "A");
        //Console.WriteLine("DFS order from A: " + string.Join(" -> ", dfsOrder));
        //// 2) Kiểm tra liên thông trước khi chạy Prim
        //Console.WriteLine("Connected? " + DFS.IsConnected(g, "A"));


        var mst = PrimMst.Compute(g, "A");

        Console.WriteLine("MST edges:");
        foreach (var e in mst)
            Console.WriteLine($"{e.From} - {e.To} (w={e.Weight})");

        Console.WriteLine($"Total weight = {PrimMst.TotalWeight(mst)}");
    }
}