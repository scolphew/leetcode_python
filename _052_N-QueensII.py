class Solution(object):
    def totalNQueens(self, n):
        """
        :type n: int
        :rtype: int
        """
        DEFAULT = -100
        board = [DEFAULT] * n
        result = 0

        def can_place(row, col):
            for index in range(n):
                if board[index] == col or abs(index - row) == abs(
                                board[index] - col):
                    return False
            return True

        i = j = 0
        while i < n:
            while j < n:
                if can_place(i, j):
                    board[i] = j
                    j = 0
                    break
                else:
                    j += 1

            if board[i] == DEFAULT:
                if i == 0:
                    break
                else:
                    i -= 1
                    j = board[i] + 1
                    board[i] = DEFAULT
                    continue
            if i == n - 1:
                result += 1
                j = board[i] + 1
                board[i] = DEFAULT
                continue
            i += 1
        return result


s = Solution()
print(s.totalNQueens(4))
