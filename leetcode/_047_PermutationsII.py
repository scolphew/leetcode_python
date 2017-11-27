class Solution(object):
    def permuteUnique(self, nums):
        """
        可以重复元素的集合， 求全排列

        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if not nums:
            return [[]]
        result = []

        def perm(start=0, end=len(nums) - 1):
            flag = set()
            if start == end:
                result.append(list(nums))
            else:
                perm(start + 1, end)
                for i in range(start + 1, end + 1):
                    if nums[start] != nums[i] and (start, nums[i]) not in flag:
                        flag.add((start, nums[i]))
                        nums[start], nums[i] = nums[i], nums[start]
                        perm(start + 1, end)
                        nums[start], nums[i] = nums[i], nums[start]

        perm()
        return result


if __name__ == '__main__':
    s = Solution()
    a = s.permuteUnique([1, 1, 2, 2, 3, 3])
    print(a)
    print(len(a))
