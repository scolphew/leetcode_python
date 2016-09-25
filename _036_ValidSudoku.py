class Solution(object):
    def isValidSudoku(self, board):
        """
        数独,判断是否合法

        :type board: List[List[str]]
        :rtype: bool
        """
        row = []
        col = []
        sub_box = []
        for i in range(9):
            for j in range(9):
                c = board[i][j]
                if c != '.':
                    if (i, c) not in row:
                        row.append((i, c))
                    else:
                        return False
                    if (j, c) not in col:
                        col.append((j, c))
                    else:
                        return False
                    if (i // 3, j // 3, c) not in sub_box:
                        sub_box.append((i // 3, j // 3, c))
                    else:
                        return False
        return True


if __name__ == '__main__':
    a = [".87654321", "3........", "3........", "4........",
         "5........", "6........", "7........", "8........",
         "9........"]
    print(Solution().isValidSudoku(a))
