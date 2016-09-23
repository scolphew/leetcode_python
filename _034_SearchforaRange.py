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
        left = 0
        right = len(nums) - 1
        while nums[left] < nums[right]:
            mid = (left + right) >> 1
            if nums[mid] > target:
                right = mid - 1
            elif nums[mid] < target:
                left = mid + 1
            else:
                if nums[left] == nums[mid]:
                    right -= 1
                else:
                    left += 1
        if nums[left] == nums[right] == target:
            return [left, right]
        return [-1, -1]

s = Solution()
print(s.searchRange([1, 2, 3, 4, 5, 5, 6], 5))
