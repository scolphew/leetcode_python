class Solution(object):
    def removeDuplicates(self, nums):
        """
        删除重复的元素（每个元素最多可以出现两次）
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) < 3:
            return len(nums)
        p = 2
        for i in nums[2:]:
            if i > nums[p - 2]:
                nums[p] = i
                p += 1
        return p


if __name__ == '__main__':
    s = Solution()
    s.removeDuplicates([1, 2, 3, 3, 3, 4, 4, 4, 4, 5, 5, 6])
