class Solution(object):
    def minDistance(self, word1, word2):
        """
        把word1转为word2，只能通过增删改字符,求最小操作数
        :type word1: str
        :type word2: str
        :rtype: int
        """
        l1 = len(word1)
        l2 = len(word2)
        if not l1:
            return l2
        if not l2:
            return l1
        flag = [[0] * (l2 + 1) for _ in range(l1 + 1)]
        for i in range(l2+1):
            flag[0][i] = i
        for i in range(l1+1):
            flag[i][0] = i
        for i in range(1, l1 + 1):
            for j in range(1, l2 + 1):
                if word1[i - 1] == word2[j - 1]:
                    flag[i][j] = flag[i - 1][j - 1]
                else:
                    flag[i][j] = 1 + min(flag[i - 1][j - 1], flag[i - 1][j],
                                         flag[i][j - 1])
        print(flag)
        return flag[-1][-1]


s = Solution()
print(s.minDistance("sea", "ate"))
