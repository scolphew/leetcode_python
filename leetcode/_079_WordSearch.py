class Solution(object):
    def exist(self, board, word):
        """
        搜索在二维数字中单词
        每个位置只能用一次
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        m, n = len(board), len(board[0])
        flag = [[False] * n for _ in range(m)]

        def search(i, j, length=0):
            if not flag[i][j] and board[i][j] == word[length]:
                if len(word)-1 == length:
                    return True
                flag[i][j] = True
                if i > 0 and not flag[i - 1][j] and search(i - 1, j,
                                                           length + 1):
                    return True
                if i < m - 1 and not flag[i + 1][j] and search(i + 1, j,
                                                               length + 1):
                    return True
                if j > 0 and not flag[i][j - 1] and search(i, j - 1,
                                                           length + 1):
                    return True
                if j < n - 1 and not flag[i][j + 1] and search(i, j + 1,
                                                               length + 1):
                    return True
                flag[i][j] = False
                return False
            else:
                return False

        for i in range(m):
            for j in range(n):
                if board[i][j] == word[0]:
                    if search(i, j):
                        return True
        return False

s = Solution()
print(s.exist([
    "ABCE","SFCS","ADEE"
], "ABCCED"))
