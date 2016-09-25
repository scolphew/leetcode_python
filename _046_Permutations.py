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


if __name__ == '__main__':
    s = Solution()
    print(s.permute([1, 2, 3]))

    a = [
        [1, 2, 3, 4], [1, 2, 4, 3], [1, 3, 2, 4], [1, 3, 4, 2], [1, 4, 2, 3],
        [1, 4, 3, 2], [2, 1, 3, 4], [2, 1, 4, 3], [2, 3, 1, 4], [2, 3, 4, 1],
        [2, 4, 1, 3], [2, 4, 3, 1], [3, 1, 2, 4], [3, 1, 4, 2], [3, 2, 1, 4],
        [3, 2, 4, 1], [3, 4, 1, 2], [3, 4, 2, 1], [4, 1, 2, 3], [4, 1, 3, 2],
        [4, 2, 1, 3], [4, 2, 3, 1], [4, 3, 1, 2], [4, 3, 2, 1]]

    b = [
        [1, 2, 3, 4], [2, 1, 3, 4], [2, 3, 1, 4], [2, 3, 4, 1], [1, 3, 2, 4],
        [3, 1, 2, 4], [3, 2, 1, 4], [3, 2, 4, 1], [1, 3, 4, 2], [3, 1, 4, 2],
        [3, 4, 1, 2], [3, 4, 2, 1], [1, 2, 4, 3], [2, 1, 4, 3], [2, 4, 1, 3],
        [2, 4, 3, 1], [1, 4, 2, 3], [4, 1, 2, 3], [4, 2, 1, 3], [4, 2, 3, 1],
        [1, 4, 3, 2], [4, 1, 3, 2], [4, 3, 1, 2], [4, 3, 2, 1]]

    a = list(map(frozenset, a))
    b = list(map(frozenset, b))
    print(a==b)

