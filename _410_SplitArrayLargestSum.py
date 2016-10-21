class Solution(object):
    def splitArray(self, nums, m):
        """
        拆分数组，分成m分
        求拆分组合和的最大值最小的拆分组合，返回差分方法
        :param nums:
        :param m:
        :return:
        """
        def valid(mid):
            cnt = 0
            current = 0
            for n in nums:
                current += n
                if current > mid:
                    cnt += 1
                    if cnt >= m:
                        return False
                    current = n
            return True

        l = max(nums)
        h = sum(nums)

        while l < h:
            mid = (l + h) >> 1
            if valid(mid):
                h = mid
            else:
                l = mid + 1
        return l


s = Solution()
a = [1,2,3]

m = 15
# print(len(a), 27407869)
print(s.splitArray(a, m))
