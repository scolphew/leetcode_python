class Solution(object):
    def search(self, nums, target):
        """
        在一个被数组中搜索target(nums无重复)
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (left + right) >> 1
            if nums[mid] == target:
                return mid
            # 左半边有序
            if nums[mid] >= nums[left]:
                # tag在左半边
                if nums[left] > target or nums[mid] <= target:
                    left = mid + 1
                else:
                    right = mid - 1
            # 右半边有序
            else:
                # tag在右半边
                if nums[right] < target or nums[mid] >= target:
                    right = mid - 1
                else:
                    left = mid + 1
        return -1
