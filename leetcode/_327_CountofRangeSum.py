class Solution(object):
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


if __name__ == '__main__':
    s = Solution()
    print(s.countRangeSum([-2, 5, -1], -2, 2))
