class Solution:
    def maximumProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max1 = max2 = max3 = -0x7fffffff
        min1 = min2 = 0x7fffffff
        for num in nums:
            if num >= max1:
                max1, max2, max3 = num, max1, max2
            elif num >= max2:
                max2, max3 = num, max2
            elif num >= max3:
                max3 = num
            if num <= min1:
                min1, min2 = num, min1
            elif num <= min2:
                min2 = num
        return max(max1 * max2 * max3, max1 * min1 * min2)
