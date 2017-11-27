class Solution(object):
    def solveNQueens(self, n):
        """
        N皇后

        :type n: int
        :rtype: List[List[str]]
        """

        def can_place(row, col):
            """
            判断第row行col列是否可以放皇后
            """
            for index in range(n):
                if board[index] == col or abs(index - row) == abs(
                                board[index] - col):
                    return False
            return True

        def toResult(lst):
            """
            格式转换，如
            [1, 3, 0, 2] -> [".Q..","...Q","Q...","..Q."]
            """
            for i in range(n):
                lst[i] = ''.join(
                    ['Q' if lst[i] == x else '.' for x in range(n)])
            return lst

        DEFAULT = -1000
        result = []
        board = [DEFAULT] * n
        i = j = 0
        while i < n:
            while j < n:  # 探测第i行可以放皇后的位置
                if can_place(i, j):
                    board[i] = j
                    j = 0
                    break
                else:
                    j += 1

            if board[i] == DEFAULT:  # 如果改行没有放皇后，回溯
                if i == 0:  # 到第0行，回溯结束
                    break
                else:  # 上移一行（行上移，皇后右移一个）
                    i -= 1
                    j = board[i] + 1
                    board[i] = DEFAULT
                    continue
            if i == n - 1:  # 最后一行，可以打印结果了
                result.append(board.copy())
                j = board[i] + 1
                board[i] = DEFAULT
                continue
            i += 1
        return [toResult(each) for each in result]


s = Solution()
print(s.solveNQueens(4))
