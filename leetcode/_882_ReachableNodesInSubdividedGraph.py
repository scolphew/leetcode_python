import collections
import heapq


class Solution:
    def reachableNodes(self, edges: list[list[int]], maxMoves: int, n: int) -> int:  # noqa
        graph = collections.defaultdict(dict)
        for u, v, w in edges:
            graph[u][v] = graph[v][u] = w

        pq = [(0, 0)]  # <a,b> 结点0到结点b的距离为a
        dist = {0: 0}  # <a:b> 结点0到结点a的当前最小距离为b
        used = {}  # <a,b>:n a->b这个边上有n个结点使用
        ans = 0

        while pq:
            d, node = heapq.heappop(pq)  # 到node的距离为d
            if d > dist[node]:
                continue
            ans += 1  # node这个结点

            for nei, weight in graph[node].items():
                v = min(weight, maxMoves - d)
                used[node, nei] = v  # node->nei这个边上有v个结点使用
                d2 = d + weight + 1
                if d2 < dist.get(nei, maxMoves + 1):
                    heapq.heappush(pq, (d2, nei))
                    dist[nei] = d2

        for u, v, w in edges:
            ans += min(w, used.get((u, v), 0) + used.get((v, u), 0))

        return ans


if __name__ == "__main__":
    s = Solution()
    y = s.reachableNodes([[0, 1, 10], [0, 2, 1], [1, 2, 2]], maxMoves=6, n=3)
    print(y)
