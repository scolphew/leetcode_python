class Solution:
    def arrayNesting(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ans = 1
        for i in range(len(nums)):
            if nums[i] < 0 or i == nums[i]:
                continue
            index, num = i, nums[i]
            tmp = 1
            while num >= 0 and nums[num] >= 0:
                tmp += 1
                nums[index] = -1
                index, num = num, nums[num]
            else:
                nums[index] = -1
            ans = max(ans, tmp)
        return ans


if __name__ == '__main__':
    s = Solution()
    print(s.arrayNesting([0, 1, 2]))
    print(s.arrayNesting([5, 4, 0, 3, 1, 6, 2]))
