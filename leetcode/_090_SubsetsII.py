class Solution(object):
    def subsetsWithDup(self, nums):
        """
        求nums的子集，nums可能含有重复元素
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if not nums:
            return [[]]
        result = [[]]
        nums.sort()
        size = 1
        last = nums[0]
        for i in nums:
            if last != i:
                last = i
                size = len(result)
            new_size = len(result)
            for j in range(new_size - size, new_size):
                result.append(result[j][:])
                result[-1].append(i)
        return result


if __name__ == '__main__':
    s = Solution()
    print(s.subsetsWithDup([1, 2, 2, 3, 3, 4]))
