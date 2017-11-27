class Solution(object):
    def numTrees(self, n):
        """
        求有n个节点的二叉查找树的种类

        :type n: int
        :rtype: int
        """
        result = [1, 1, 2, 5]
        if n < 4:
            return result[n]

        for i in range(4, n + 1):
            result.append(sum(result[j] * result[i - j - 1] for j in range(i)))
        return result[n]


if __name__ == '__main__':
    s = Solution()
    s.numTrees(6)
