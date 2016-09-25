class Solution(object):
    def solveSudoku(self, board):
        """
        计算数独

        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        for i in range(9):
            board[i] = [c for c in board[i]]

        row = [set(range(1, 10)) for i in range(9)]
        col = [set(range(1, 10)) for i in range(9)]
        sub = [[set(range(1, 10)) for i in range(3)] for j in range(3)]

        count = 0  # 记录空格数量
        for i in range(9):
            for j in range(9):
                c = board[i][j]
                if c != '.':
                    row[i].remove(int(c))
                    col[j].remove(int(c))
                    sub[i // 3][j // 3].remove(int(c))
                else:
                    count += 1

        def dfs(i, j, count):
            if not count:
                return True

            while board[i][j] != '.':
                if j == 8:
                    j = 0
                    i += 1
                else:
                    j += 1

            choose = row[i] & col[j] & sub[i // 3][j // 3]
            for c in choose:
                board[i][j] = str(c)
                row[i].remove(c)
                col[j].remove(c)
                sub[i // 3][j // 3].remove(c)
                if dfs(i, j, count - 1):
                    return True
                row[i].add(c)
                col[j].add(c)
                sub[i // 3][j // 3].add(c)
                board[i][j] = '.'
            return False

        dfs(0, 0, count)
        for i in range(9):
            board[i] = ''.join(board[i])


def p(board):
    for i in range(9):
        for j in range(9):
            print(
                int(board[i][j]) if board[i][j] != '.' else '_',
                end=' ')
        print()


if __name__ == '__main__':
    s = Solution()
    a = ["53..7....", "6..195...", ".98....6.",
         "8...6...3", "4..8.3..1", "7...2...6",
         ".6....28.", "...419..5", "....8..79"]
    s.solveSudoku(a)
    print(a)

    a = set([1, 2, 3])
