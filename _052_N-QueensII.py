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

    def totalNQueens2(self, n):
        def dfs(row, path, cols, xySum, xyDif, n):
            result = 0
            if row == n:
                return 1
            for col in range(n):
                if col not in cols and (row + col) not in xySum and (
                            row - col) not in xyDif:
                    cols.add(col)
                    xySum.add(row + col)
                    xyDif.add(row - col)
                    result += dfs(row + 1, path + [col], cols, xySum, xyDif, n)
                    cols.remove(col)
                    xySum.remove(row + col)
                    xyDif.remove(row - col)
            return result

        matrix = []
        res = []
        return dfs(0, [], set(), set(), set(), n)


s = Solution()
print(s.totalNQueens(4))
