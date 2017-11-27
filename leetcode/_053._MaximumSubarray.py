class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # if not nums:
        #     return None
        max1 = result = nums[0]
        for i in nums[1:]:
            max1 = max1 + i if max1 + i > i else i
            # result = max1 if max1 > result else result
            # if i > 0:
            #     max1 = max1 + i if max1 + i > i else i
            # else:
            #     if max1 + i < i:
            #         max1 = i
            #     else:
            #         max1 += i
            if max1 > result:
                result = max1
        return result


if __name__ == '__main__':
    s = Solution()
    print(s.maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4]))
