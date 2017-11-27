class Solution(object):
    def firstMissingPositive(self, nums):
        """
        无序的数组，返回缺失的第一个整正数

        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 1
        index = 0
        while index < len(nums):
            if index + 1 == nums[index]:
                index += 1
                continue
            if 0 < nums[index] <= len(nums):
                index_1 = nums[index]
                while 0 < index_1 <= len(nums) and index_1 != nums[
                            index_1 - 1]:
                    x = nums[index_1 - 1]
                    nums[index_1 - 1] = index_1
                    index_1 = x
            index += 1

        i = 0
        while i < len(nums):
            if nums[i] != i + 1:
                return i + 1
            i += 1
        return len(nums) + 1


if __name__ == '__main__':
    s = Solution()
    print(s.firstMissingPositive([1, 2, 3, 4, 5, 6]))
    print(s.firstMissingPositive([0, 1, 2, 3, 4, 5, 7]))
    print(s.firstMissingPositive([0, -1, 2, 3, 4, 5, 7]))
    print(s.firstMissingPositive([3, 4, -1, 1]))
    print(s.firstMissingPositive([1, 2, 2, 5, 7]))
    print(s.firstMissingPositive([2, 1]))
    print(s.firstMissingPositive([2]))
    print(s.firstMissingPositive([1]))
