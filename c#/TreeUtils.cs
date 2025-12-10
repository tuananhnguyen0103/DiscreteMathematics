// TreeUtils.cs
using System;
using System.Collections.Generic;
using System.Linq;

namespace GraphTreeDemo
{
    public static class TreeUtils
    {
        /// <summary>
        /// Kiểm tra đồ thị có liên thông hay không bằng BFS.
        /// </summary>
        public static bool IsConnected(Graph graph)
        {
            var vertices = graph.Vertices;

            if (vertices.Count == 0)
                return false;

            string start = vertices[0];
            var visited = new HashSet<string>();
            var queue = new Queue<string>();

            queue.Enqueue(start);

            while (queue.Count > 0)
            {
                string u = queue.Dequeue();

                if (visited.Contains(u))
                    continue;

                visited.Add(u);

                foreach (var v in graph.Neighbors(u))
                {
                    if (!visited.Contains(v))
                    {
                        queue.Enqueue(v);
                    }
                }
            }

            return visited.Count == vertices.Count;
        }

        /// <summary>
        /// Kiểm tra đồ thị có phải là Tree (cây) hay không:
        /// - Tree vô hướng ⇔ liên thông và số cạnh = số đỉnh - 1.
        /// </summary>
        public static bool IsTree(Graph graph)
        {
            int n = graph.Vertices.Count;
            int m = graph.Edges.Count;

            if (m != n - 1)
                return false;

            if (!IsConnected(graph))
                return false;

            return true;
        }

        /// <summary>
        /// Trả về thứ tự duyệt DFS (danh sách các đỉnh).
        /// </summary>
        public static List<string> DfsOrder(Graph graph, string start)
        {
            var order = new List<string>();
            var visited = new HashSet<string>();

            void Dfs(string u)
            {
                visited.Add(u);
                order.Add(u);

                if (!graph.Adj.ContainsKey(u))
                    return;

                foreach (var (v, _) in graph.Adj[u])
                {
                    if (!visited.Contains(v))
                    {
                        Dfs(v);
                    }
                }
            }

            if (graph.Adj.ContainsKey(start))
            {
                Dfs(start);
            }

            return order;
        }

        /// <summary>
        /// Tạo spanning tree bằng DFS, trả về danh sách cạnh (u, v, w).
        /// </summary>
        public static List<(string U, string V, int W)> SpanningTreeDfs(Graph graph, string start)
        {
            var treeEdges = new List<(string U, string V, int W)>();
            var visited = new HashSet<string>();

            void Dfs(string u)
            {
                visited.Add(u);

                if (!graph.Adj.ContainsKey(u))
                    return;

                foreach (var (v, w) in graph.Adj[u])
                {
                    if (!visited.Contains(v))
                    {
                        // Cạnh này thuộc spanning tree
                        treeEdges.Add((u, v, w));
                        Dfs(v);
                    }
                }
            }

            if (graph.Adj.ContainsKey(start))
            {
                Dfs(start);
            }

            return treeEdges;
        }

        /// <summary>
        /// Prim's Algorithm để tìm Minimum Spanning Tree từ đỉnh start.
        /// Trả về danh sách cạnh (u, v, w) của MST.
        /// </summary>
        public static List<(string U, string V, int W)> PrimMst(Graph graph, string start)
        {
            var mstEdges = new List<(string U, string V, int W)>();
            var vertices = graph.Vertices;

            if (vertices.Count == 0 || !graph.Adj.ContainsKey(start))
                return mstEdges;

            var inMst = new HashSet<string> { start };

            // Lặp cho đến khi tất cả đỉnh đều nằm trong MST
            while (inMst.Count < vertices.Count)
            {
                string bestU = null;
                string bestV = null;
                int bestW = int.MaxValue;
                bool found = false;

                // Tìm cạnh có trọng số nhỏ nhất nối từ tập inMst ra ngoài
                foreach (var u in inMst)
                {
                    foreach (var (v, w) in graph.Adj[u])
                    {
                        if (!inMst.Contains(v) && w < bestW)
                        {
                            bestW = w;
                            bestU = u;
                            bestV = v;
                            found = true;
                        }
                    }
                }

                // Nếu không tìm được cạnh nào nữa thì đồ thị không liên thông
                if (!found)
                {
                    break;
                }

                // Thêm cạnh tốt nhất vào MST
                mstEdges.Add((bestU, bestV, bestW));
                inMst.Add(bestV);
            }

            return mstEdges;
        }
    }
}
