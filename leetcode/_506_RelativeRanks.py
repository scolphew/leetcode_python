class Solution(object):
    def findRelativeRanks(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        sort = sorted(nums)[::-1]
        rank = ["Gold Medal", "Silver Medal", "Bronze Medal"] + list(
            map(str, range(4, len(nums) + 1)))
        d = dict(zip(sort, rank))
        return [d[num] for num in nums]


if __name__ == '__main__':
    s = Solution()
    print(s.findRelativeRanks([4, 5, 3, 1, 2]))
