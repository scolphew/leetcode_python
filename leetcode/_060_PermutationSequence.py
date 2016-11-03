import math


class Solution(object):
    def getPermutation(self, n, k):
        """
        给一个数字n，返回1-n组成的数字的第k个
        :type n: int
        :type k: int
        :rtype: str
        """
        nums = [str(_) for _ in range(1, n + 1)]
        factorial = [1]
        for i in range(2, n + 1):
            factorial.append(i * factorial[i - 2])
        result = ""
        for i in range(n - 1, 0, -1):
            index = (k - 1) // factorial[i - 1]
            k %= factorial[i - 1]
            result += nums.pop(index)
        result += nums[0]
        return result

s = Solution()
for ii in range(1, 6):
    for j in range(1, math.factorial(ii) + 1):
        print(ii, "-", j, end="  ")
        print(s.getPermutation(ii, j))
