class Solution(object):
    def findRotateSteps(self, ring, key):
        """
        :type ring: str
        :type key: str
        :rtype: int
        """
        MAX = 0xffffffff
        from collections import defaultdict
        dp = [[0] * len(ring) for _ in range(len(key))]
        d = defaultdict(list)
        n = len(ring)
        len_key = len(key)
        for i, c in enumerate(ring):
            d[c].append(i)
        for i in d[key[0]]:
            dp[0][i] = min(i, n - i)

        former = key[0]
        for i in range(1, len_key):
            cur = key[i]
            for index_cur in d[cur]:
                dp[i][index_cur] = MAX
                for index_former in d[former]:
                    distance = abs(index_cur - index_former)
                    dp[i][index_cur] = min(dp[i][index_cur],
                                           dp[i - 1][index_former] + min(
                                               distance, n - distance))
            former = cur

        ans = MAX

        for i in d[key[-1]]:
            if ans > dp[len_key - 1][i]:
                ans = dp[len_key - 1][i]
        return ans + len_key


if __name__ == '__main__':
    s = Solution()
    print(s.findRotateSteps("godding", "gd"))
