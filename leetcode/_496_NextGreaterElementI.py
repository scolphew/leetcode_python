from typing import List


class Solution(object):
    def nextGreaterElement(self, findNums, nums):
        """
        :type findNums: List[int]
        :type nums: List[int]
        :rtype: List[int]
        """
        map = {}
        stack = []
        for num in nums:
            while stack and stack[-1] < num:
                map[stack.pop()] = num
            stack.append(num)

        ans = []
        for i in findNums:
            ans.append(map.get(i, -1))
        return ans


if __name__ == '__main__':
    s = Solution()
    print(s.nextGreaterElement([4, 1, 2], [1, 4, 2, 7]))
