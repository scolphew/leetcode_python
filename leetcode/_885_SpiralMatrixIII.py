class Solution:
    def spiralMatrixIII(self, rows: int, cols: int, rStart: int, cStart: int) -> list[list[int]]:  # noqa
        ans = [[rStart, cStart]]

        k = 1
        step = 1
        while k < rows * cols:
            # 右
            for _ in range(step):
                cStart += 1
                if 0 <= rStart < rows and 0 <= cStart < cols:
                    ans.append([rStart, cStart])
                    k += 1
            # 下
            for _ in range(step):
                rStart += 1
                if 0 <= rStart < rows and 0 <= cStart < cols:
                    ans.append([rStart, cStart])
                    k += 1

            step += 1

            # 左
            for _ in range(step):
                cStart -= 1
                if 0 <= rStart < rows and 0 <= cStart < cols:
                    ans.append([rStart, cStart])
                    k += 1
            # 上
            for _ in range(step):
                rStart -= 1
                if 0 <= rStart < rows and 0 <= cStart < cols:
                    ans.append([rStart, cStart])
                    k += 1
            step += 1
        return ans


if __name__ == "__main__":
    s = Solution()
    y = s.spiralMatrixIII(5, 6, 1, 4)
    print(y)
