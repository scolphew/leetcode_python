import search


class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        left = search.search_first(nums, target)
        right = search.search_last(nums, target)
        return [left, right]


s = Solution()
print(s.searchRange([1, 2, 3, 4, 5, 5, 6], 5))
