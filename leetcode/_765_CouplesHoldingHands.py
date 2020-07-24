from typing import List


class Solution:
    def minSwapsCouples(self, row: List[int]) -> int:
        d = {v: k for k, v in enumerate(row)}
        ans = 0
        for i in range(len(row) // 2):
            if row[i * 2] // 2 != row[i * 2 + 1] // 2:
                t = d[(row[i * 2] // 2 * 2) + (1 - row[i * 2] & 1)]
                d[row[i * 2 + 1]], row[i * 2 + 1], row[t] = t, row[t], row[ i * 2 + 1]
                ans += 1
        return ans


if __name__ == '__main__':
    s = Solution()
    print(s.minSwapsCouples([0, 2, 4, 6, 7, 1, 3, 5]))
