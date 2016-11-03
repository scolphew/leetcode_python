from base import search


class Solution(object):
    """
    先找到某一个值，在向两边扩展
    """

    def searchRange(self, nums, target):
        """
        返回nums中target最左和最右的下标

        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        left = search.search_first(nums, target)
        if left == -1:
            return [-1, -1]
        right = left
        while right < len(nums) and nums[right] == target:
            right += 1
        return [left, right - 1]


s = Solution()
print(s.searchRange([1, 2, 3, 4,  5, 6], 5))
