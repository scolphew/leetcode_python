from collections import defaultdict


class Solution:
    def possibleBipartition(self, n: int, dislikes: list[list[int]]) -> bool:  # noqa
        lst = defaultdict(list)
        for a, b in dislikes:
            lst[a].append(b)
            lst[b].append(a)

        color = {}

        def dfs(node: int, c=1) -> bool:
            if node in color:
                return color[node] == c
            color[node] = c
            # for nei in lst[node]:
            #     if not dfs(nei, c ^ 1): # 邻居按另一种颜色
            #         return False
            # return True
            return all(dfs(nei, c ^ 1) for nei in lst[node])

        # for node_ in range(1, n + 1):
        #     if node_ not in color and not dfs(node_, 0): # 新的连通分量
        #         return False
        # return True
        return all(dfs(node_, 0) for node_ in range(1, n + 1) if node_ not in color)


if __name__ == "__main__":
    s = Solution()
    y = s.possibleBipartition(4, [[1, 2], [1, 3], [2, 4]])
    print(y)
