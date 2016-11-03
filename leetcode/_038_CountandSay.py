class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        res = "1"
        for i in range(n - 1):
            tmp = ""
            current = res[0]
            current_count = 1
            for j in res[1:]:
                if j == current:
                    current_count += 1
                else:
                    tmp += str(current_count) + current
                    current = j
                    current_count = 1
            else:
                tmp += str(current_count) + current
            res = tmp
        return res


s = Solution()
print(s.countAndSay(10))
