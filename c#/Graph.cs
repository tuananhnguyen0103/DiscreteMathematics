// Graph.cs
using System;
using System.Collections.Generic;
using System.Linq;

namespace GraphTreeDemo
{
    /// <summary>
    /// Đồ thị vô hướng có trọng số, cài đặt bằng danh sách kề.
    /// </summary>
    public class Graph
    {
        // adj: mỗi đỉnh -> danh sách các (đỉnh_kề, trọng_số)
        // Ví dụ: adj["A"] = [("B", 3), ("C", 5)]
        public Dictionary<string, List<(string To, int Weight)>> Adj { get; }
            = new Dictionary<string, List<(string To, int Weight)>>();

        // Danh sách cạnh: (u, v, w)
        public List<(string U, string V, int W)> Edges { get; }
            = new List<(string U, string V, int W)>();

        /// <summary>
        /// Danh sách các đỉnh trong đồ thị.
        /// </summary>
        public List<string> Vertices
        {
            get { return Adj.Keys.ToList(); }
        }

        /// <summary>
        /// Thêm đỉnh nếu chưa tồn tại.
        /// </summary>
        public void AddVertex(string v)
        {
            if (!Adj.ContainsKey(v))
            {
                Adj[v] = new List<(string To, int Weight)>();
            }
        }

        /// <summary>
        /// Thêm cạnh vô hướng (u, v) với trọng số w.
        /// Cập nhật danh sách kề và danh sách cạnh.
        /// </summary>
        public void AddEdge(string u, string v, int w = 1)
        {
            // Đảm bảo 2 đỉnh tồn tại
            AddVertex(u);
            AddVertex(v);

            // Thêm vào danh sách kề (vô hướng)
            Adj[u].Add((v, w));
            Adj[v].Add((u, w));

            // Chuẩn hóa cạnh để tránh trùng (u, v) và (v, u)
            string a = u;
            string b = v;
            if (string.Compare(a, b, StringComparison.Ordinal) > 0)
            {
                // Nếu a > b thì hoán đổi, bảo đảm a <= b
                var tmp = a;
                a = b;
                b = tmp;
            }

            var edge = (U: a, V: b, W: w);

            // Chỉ thêm nếu chưa có cạnh này trong danh sách
            if (!Edges.Contains(edge))
            {
                Edges.Add(edge);
            }
        }

        /// <summary>
        /// Trả về danh sách các đỉnh kề của v (bỏ qua trọng số).
        /// </summary>
        public IEnumerable<string> Neighbors(string v)
        {
            if (!Adj.ContainsKey(v))
                return Enumerable.Empty<string>();

            return Adj[v].Select(p => p.To);
        }
    }
}
