class Solution(object):
    def nextGreaterElements(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        ans = [-1] * n

        stack = []
        for i in range(n * 2):
            num = nums[i % n]
            while stack and nums[stack[-1]] < num:
                ans[stack.pop()] = num
            if i < n:
                stack.append(i)
        return ans


if __name__ == '__main__':
    s = Solution()
    print(s.nextGreaterElements([100, 1, 11, 1, 120, 111, 123, 1, -1, -100]))
