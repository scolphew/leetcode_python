class Solution:
    def lenLongestFibSubseq(self, arr: list[int]) -> int:  # noqa
        index = {num: i for i, num in enumerate(arr)}
        ans = 0
        n = len(arr)
        dp = [[0] * n for _ in range(n)]  # dp[a][b] 表示以arr中最后两个位置是ab时最长数列
        for i, num_i in enumerate(arr[2:], 2):
            for j in range(i - 1, -1, -1):
                num_j = arr[j]
                if num_j * 2 <= num_i:
                    break
                if (num_k := num_i - num_j) in index:  # k<j<i
                    k = index[num_k]
                    dp[j][i] = max(dp[k][j] + 1, 3)
                    ans = max(ans, dp[j][i])
        return ans


if __name__ == "__main__":
    s = Solution()
    y = s.lenLongestFibSubseq([1, 3, 7, 11, 12, 14, 18])
    print(y)
