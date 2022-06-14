from typing import List


class Solution:
    def sumOfDistancesInTree(self, n: int, edges: List[List[int]]) -> List[int]:  # noqa
        ans = [0] * n
        dp = [0] * n  # 作为根到到子节点的距离
        sz = [0] * n  # 作为根的子树节点数量
        graph = [[] for _ in range(n)]

        # 图/树
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        def dfs1(u1=0, father=-1):
            sz[u1] = 1
            dp[u1] = 0
            for v1 in graph[u1]:
                if v1 == father:
                    continue
                dfs1(v1, u1)
                dp[u1] += dp[v1] + sz[v1]  # 加孩子的字数结点距离，每个孩子再加上1(u,v的距离)
                sz[u1] += sz[v1]  # 加字数结点数

        def dfs2(u2=0, father=-1):
            ans[u2] = dp[u2]  # 当前的距离
            for v2 in graph[u2]:
                if v2 == father:
                    continue
                tmp = dp[u2], dp[v2], sz[u2], sz[v2]  # 保存
                dp[u2] -= dp[v2] + sz[v2]  # 减去距离，每个孩子再减去1
                sz[u2] -= sz[v2]  # 减去子树节点数
                # 最终 dp[v2] = dp[u2] + sz[u2] - 2*sz[v2]
                # sz[u2]-sz[v2](u2中除z2子树之外的结点每个距离+1)
                # dp[u2]-sz[v2](u2到v2子树的距离，变为v2到每个子树的距离，每个减一)
                dp[v2] += dp[u2] + sz[u2]
                sz[v2] += sz[u2]  # 最终 sz[v2] = sz[u2]
                dfs2(v2, u2)
                dp[u2], dp[v2], sz[u2], sz[v2] = tmp  # 复原

        dfs1()
        dfs2()

        return ans


if __name__ == '__main__':
    s = Solution()
    x = s.sumOfDistancesInTree(6, [[0, 1], [0, 2], [2, 3], [2, 4], [2, 5]])
    print(x)
