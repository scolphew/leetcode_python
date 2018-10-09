class Solution(object):
    def findRedundantDirectedConnection(self, edges):
        import collections
        N = len(edges)
        parent = {}
        candidates = []  # 两条边 相同的儿子
        for u, v in edges:
            if v in parent:
                candidates.append((parent[v], v))
                candidates.append((u, v))
            else:
                parent[v] = u

        def orbit(node):
            """
            寻找根节点
            """
            seen = set()
            while node in parent and node not in seen:
                seen.add(node)
                node = parent[node]
            return node, seen

        root = orbit(1)[0]  # 根节点

        # 如果 没有同一结点有两个父节点，说明存在环，删除环上任意边都可成树
        if not candidates:
            cycle = orbit(root)[1]  # 找到环上的任意结点
            # 找到输入中最后一个环上的边，返回
            for u, v in edges:
                if u in cycle and v in cycle:
                    ans = u, v
            return ans

        children = collections.defaultdict(list)
        for v in parent:
            children[parent[v]].append(v)

        # 宽度优先遍历
        seen = [True] + [False] * N
        stack = [root]
        while stack:
            node = stack.pop()
            if not seen[node]:
                seen[node] = True
                stack.extend(children[node])

        # 如果能够遍历，则seen全为T，则输出后出现的那条便，否则，输出另一条
        return candidates[all(seen)]


if __name__ == '__main__':
    s = Solution()
    print(s.findRedundantDirectedConnection([
        [4, 2],
        [4, 3],
        [2, 6],
        [6, 7],
        [7, 8],
        [8, 6],
        [3, 1],
        [3, 5],
    ]))
