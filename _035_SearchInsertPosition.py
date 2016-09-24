class Solution(object):
    def searchInsert(self, nums, target):
        """
        返回有序链表中target的索引，如果不存在，则返回应该插入的位置

        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        left = 0
        right = lenhth = len(nums) - 1
        while left < right:
            mid = (left + right) >> 1
            if nums[mid] < target:
                left = mid + 1
            else:
                right = mid

        if left == lenhth and nums[left] < target:
            return left + 1

        return left


if __name__ == '__main__':
    s = Solution()
    print(s.searchInsert([1, 2, 3, 4, 6, 6, 7], 8))
