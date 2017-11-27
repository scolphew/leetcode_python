class Solution(object):
    def subsets(self, nums):
        """
        求子集
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        result = [[]]
        for i in nums:
            x = [k for k in result]
            for sub in x:
                result.append(sub + [i])
        return result


if __name__ == '__main__':
    s = Solution()
    print(s.subsets([1, 2]))
