from base.base import run_time


class Solution(object):
    @run_time
    def countRangeSum(self, nums, lower, upper):
        """
        :type nums: List[int]
        :type lower: int
        :type upper: int
        :rtype: int
        """
        if not nums:
            return 0
        length = len(nums)
        sums = [0] * length
        sums[0] = nums[0]
        for i in range(1, length):
            sums[i] = sums[i - 1] + nums[i]

        def merge(start=0, end=length):
            if start >= end:
                return 0
            if end - start == 1:
                if lower <= sums[start] <= upper:
                    return 1
                else:
                    return 0

            mid = (start + end) >> 1
            res = merge(start, mid) + merge(mid, end)
            tmp = []
            t = l = r = mid
            for i in range(start, mid):
                while l < end and sums[l] - sums[i] < lower:
                    l += 1
                while r < end and sums[r] - sums[i] <= upper:
                    r += 1
                while t < end and sums[t] < sums[i]:
                    tmp.append(sums[t])
                    t += 1
                tmp.append(sums[i])
                res += (r - l)
            tmp.extend(sums[t:end])
            tmp_len = end - start
            sums[start:start + tmp_len] = tmp
            return res

        return merge()

    @run_time
    def f2(self, nums, lower, upper):
        first = [0]
        for num in nums:
            first.append(first[-1] + num)

        def merge(lo=0, hi=len(first)):
            mid = (lo + hi) >> 1
            if mid == lo:
                return 0
            count = merge(lo, mid) + merge(mid, hi)
            i = j = mid
            for left in first[lo:mid]:
                while i < hi and first[i] - left < lower:
                    i += 1
                while j < hi and first[j] - left <= upper:
                    j += 1
                count += j - i
            first[lo:hi] = sorted(first[lo:hi])
            return count

        return merge()


if __name__ == '__main__':
    s = Solution()
    nums = []
    for i in range(10000):
        lst = [i for i in range(-100, 100)]
        nums.extend(lst)
    print(len(nums))
    a = (nums, -20, 20)
    print(s.f2(*a))
    print(s.countRangeSum(*a))
