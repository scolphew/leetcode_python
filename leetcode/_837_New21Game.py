class Solution:
    def new21Game(self, n: int, k: int, maxPts: int) -> float:  # noqa
        """
        k: 得分小于k则继续抽
        n: 分数不超过n的概率
        maxPts: 最大得分
        """
        if k == 0:  # 不需要抽
            return 1
        if k - 1 + maxPts <= n:  # 最后一抽之后仍然不会超过
            return 1

        # k - 1 + maxPts > n

        # dp[x] 表示从得分为 x 的情况开始游戏并且获胜的概率
        # 0 --> (k-2) --> (k-1) --> (k --> n) --> (n+1 --> k+maxPts)
        dp = [0.0] * (k + maxPts)

        # 得分已经大于等于k且小于n，此时概率为1
        # dp[x]=1(x<=k<=n)
        for i in range(k, n + 1):
            dp[i] = 1.0
        # dp[x=0](n<=x<k+maxPts) 已经输了，但还是要抽

        # dp[x]=sum(dp[x+i] for i in range(1,maxPts+1))/maxPts (0<=x<k) 从x开始每种得分的概率均值
        # dp[x]-dp[x+1]=(dp[x+1]-dp[x+maxPts+1])/maxPts (0<=x<k-1)

        # dp[k-1] = sum(dp[k-1+i] for i in range(maxPts+1))/maxPts
        #         = sum(dp[k]+...+dp[k-1+maxPts+1])/maxPts
        #         = sum(dp[k]+...+dp[k+maxPts])/maxPts
        #         = sum(dp[k]+...+dp[n]+...+dp[k+maxPts])/maxPts # 前半部分(dp[k->n])为1 后半部分为0
        dp[k - 1] = (n - k + 1) / maxPts

        # dp[k-1] 到 dp[0]
        for i in range(k - 2, -1, -1):
            dp[i] = dp[i + 1] - (dp[i + maxPts + 1] - dp[i + 1]) / maxPts
        return dp[0]


if __name__ == '__main__':
    s = Solution()
    y = s.new21Game(21, 17, 10)
    print(y)
