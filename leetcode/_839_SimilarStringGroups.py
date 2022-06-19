from typing import List


class Solution:
    def numSimilarGroups(self, strs: List[str]) -> int:  # noqa
        """
        :param strs: 列表中的每个字符串都是 strs 中其它所有字符串的一个字母异位词
        :return: 相似字符串组数量
        """

        def similar(s1: str, s2: str):
            diff = 0
            for c1, c2 in zip(s1, s2):
                if c1 != c2:
                    diff += 1
                    if diff > 2: return False
            return True

        n = len(strs)
        father = list(range(n))

        def find(index_: int) -> int:
            if father[index_] == index_: return index_
            father[index_] = find(father[index_])
            return father[index_]

        for i in range(n):
            for j in range(i + 1, n):
                fi, fj = find(i), find(j)
                if fi == fj: continue
                if similar(strs[i], strs[j]): father[fi] = fj
        return sum(1 for i in range(n) if father[i] == i)


if __name__ == '__main__':
    s = Solution()
    x = s.numSimilarGroups(["tars", "rats", "arts", "star"])
    print(x)
