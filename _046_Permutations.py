class Solution(object):
    def permute(self, nums):
        """
        给一个不同数字的集合，返回所有可能的排列

        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if not nums:
            return [[]]
        if len(nums) == 1:
            return [nums]
        result = []
        for i in nums:
            x = list(nums)
            x.remove(i)
            for each in self.permute(x):
                result.append([i] + each)

        return result

    def permute2(self, nums):
        result = []
        if not nums:
            return [[]]

        def perm(start, end):
            if start == end:
                lst = list(nums)
                result.append(lst)
            else:
                perm(start + 1, end)
                for i in range(start + 1, end + 1):
                    nums[i], nums[start] = nums[start], nums[i]
                    perm(start + 1, end)
                    nums[i], nums[start] = nums[start], nums[i]

        perm(0, len(nums) - 1)
        return result


if __name__ == '__main__':
    s = Solution()
    a = s.permute([1, 2, 3, 4, 5])
    b = s.permute2([1, 2, 3, 4, 5])

    from equal import equal_list_list

    print(equal_list_list(a, b))