class Solution:
    def consecutiveNumbersSum(self, n: int) -> int:  # noqa
        ans = 1
        k = 2
        while (k * (k + 1)) >> 1 <= n:
            if k & 1:  # 奇数个连续和
                ans += 0 if n % k else 1  # 整除即可满足条件
            else:  # 偶数个连续和
                # n % k != 0 and 2n % k == 0
                # 既 n / k = n // k + 0.5
                # 从 n//k 和 n//k+1 两边展开
                ans += 1 if n % k == k >> 1 else 0
            k += 1
        return ans


if __name__ == '__main__':
    s = Solution()
    y = s.consecutiveNumbersSum(8)
    print(y)
