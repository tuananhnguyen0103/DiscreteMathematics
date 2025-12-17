using Prim.Models;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Prim.Graph
{
    public class Graph
    {
        // Adjacency List: Adj[u] = list các cạnh đi ra từ u
        public Dictionary<string, List<Edge>> Adj { get; } = new();

        public void AddVertex(string v)
        {
            if (!Adj.ContainsKey(v))
                Adj[v] = new List<Edge>();
        }

        // Đồ thị vô hướng có trọng số
        public void AddEdge(string u, string v, int w)
        {
            AddVertex(u);
            AddVertex(v);

            Adj[u].Add(new Edge(v, w));
            Adj[v].Add(new Edge(u, w));
        }

        public int VertexCount => Adj.Count;

        public bool ContainsVertex(string v) => Adj.ContainsKey(v);

        public IEnumerable<Edge> NeighborsOf(string v)
        {
            if (!Adj.ContainsKey(v))
                throw new ArgumentException($"Vertex '{v}' does not exist.");
            return Adj[v];
        }
    }
}
