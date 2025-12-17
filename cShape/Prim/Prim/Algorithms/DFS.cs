using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Prim.Algorithms
{
    public static class DFS
    {
        // DFS duyệt toàn bộ từ start
        public static List<string> Dfs(Graph.Graph g, string start)
        {
            var order = new List<string>();
            var visited = new HashSet<string>();
            var stack = new Stack<string>();

            stack.Push(start);

            while (stack.Count > 0)
            {
                var u = stack.Pop();
                if (visited.Contains(u)) continue;

                visited.Add(u);
                order.Add(u);

                // Push neighbors (để thứ tự ổn định, có thể sort nếu cần)
                foreach (var e in g.NeighborsOf(u))
                {
                    if (!visited.Contains(e.To))
                        stack.Push(e.To);
                }
            }

            return order;
        }

        // Kiểm tra liên thông bằng DFS
        public static bool IsConnected(Graph.Graph g, string start)
        {
            var visitedOrder = Dfs(g, start);
            return visitedOrder.Count == g.VertexCount;
        }
    }
}
