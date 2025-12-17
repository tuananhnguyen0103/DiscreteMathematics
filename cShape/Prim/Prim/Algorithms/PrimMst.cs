using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using Prim.Models;
using Prim.Graph;
namespace Prim.Algorithms
{
    public static class PrimMst
    {
        public static List<MstEdge> Compute(Graph.Graph g, string start)
        {
            if (!g.ContainsVertex(start))
                throw new ArgumentException($"Start vertex '{start}' does not exist in graph.");

            var visited = new HashSet<string>();
            var mst = new List<MstEdge>();

            // Min-heap theo trọng số (priority = Weight)
            var pq = new PriorityQueue<ProposedEdge, int>();

            // 1) Bắt đầu
            visited.Add(start);

            // 2) Đẩy các cạnh từ start vào heap
            foreach (var e in g.NeighborsOf(start))
                pq.Enqueue(new ProposedEdge(start, e.To, e.Weight), e.Weight);

            // 3) Lặp đến khi đủ đỉnh (hoặc heap cạn)
            while (visited.Count < g.VertexCount && pq.Count > 0)
            {
                var cand = pq.Dequeue();

                // Nếu To đã nằm trong MST -> bỏ qua (tránh chu trình)
                if (visited.Contains(cand.To))
                    continue;

                // Chọn cạnh này
                visited.Add(cand.To);
                mst.Add(new MstEdge(cand.From, cand.To, cand.Weight));

                // Cập nhật biên: thêm các cạnh đi từ đỉnh mới vào heap
                foreach (var e in g.NeighborsOf(cand.To))
                {
                    if (!visited.Contains(e.To))
                        pq.Enqueue(new ProposedEdge(cand.To, e.To, e.Weight), e.Weight);
                }
            }

            // Nếu đồ thị không liên thông: không thể có MST đủ đỉnh
            if (mst.Count != g.VertexCount - 1)
                throw new InvalidOperationException("Graph is not connected, cannot build MST covering all vertices.");

            return mst;
        }

        public static int TotalWeight(List<MstEdge> mst)
        {
            int sum = 0;
            foreach (var e in mst) sum += e.Weight;
            return sum;
        }
    }
}
