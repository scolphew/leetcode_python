class Solution(object):
    def findRedundantDirectedConnection(self, edges):
        from collections import defaultdict
        parent_of = {}
        candidates = []

        for parent, child in edges:
            if child in parent_of:
                candidates.append([parent_of[child], child])
                candidates.append([parent, child])
            else:
                parent_of[child] = parent

        if candidates:
            # 如果有一个结点有两个双亲
            # 如果第一条边在环内（即根不在环上,或者说，成为了某一非根祖先父节点），返回该边。
            # 否则（即菱形关系）返回另一条
            u, v = candidates[0]
            while u != v and u in parent_of:
                u = parent_of[u]
            # u==v 则有环（根不在环上） 返回前一个
            # u!=v 无环 返回后一个,
            return candidates[u != v]
        else:
            # 有环，根在环上
            s = set()
            root = 1
            while root in parent_of and root not in s:
                # 有双亲且未访问
                s.add(root)
                root = parent_of[root]
            s = set()
            while root in parent_of and root not in s:
                s.add(root)
                root = parent_of[root]
            for u, v in edges[::-1]:
                if u in s and v in s:
                    return [u, v]


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

    print(s.findRedundantDirectedConnection(
        [[1, 2], [2, 3], [3, 4], [4, 1], [1, 5]]
    ))
