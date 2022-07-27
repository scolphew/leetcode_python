class Solution:
    def profitableSchemes(self, n: int, minProfit: int, group: list[int], profit: list[int]) -> int:  # noqa
        MOD = 10 ** 9 + 7  # noqa

        crimes_num = len(group)  # 工作数量
        dp = [[[0] * (minProfit + 1) for _ in range(n + 1)] for _ in range(crimes_num + 1)]
        dp[0][0][0] = 1  # <i,j,k> 前i个工作 选了j个员工 且利润大于等于k
        for i in range(1, crimes_num + 1):
            members, profit_i1 = group[i - 1], profit[i - 1]  # 第(i-1)个工作需要的人，利润
            for j in range(n + 1):
                for k in range(minProfit + 1):
                    if j < members:  # 不选择该工作
                        dp[i][j][k] = dp[i - 1][j][k]
                    else:  # 选择 和 不选择的和
                        dp[i][j][k] = (dp[i - 1][j][k] + dp[i - 1][j - members][max(0, k - profit_i1)]) % MOD

        total = sum(dp[crimes_num][j][minProfit] for j in range(n + 1)) % MOD
        return total
