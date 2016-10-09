class Solution(object):
    def canJump(self, nums):
        """
        当前索引表示最大的跳数，求到达终点的最小跳数
        每一次挑选下一步能调的最远的地方
        :type nums: List[int]
        :rtype: bool
        """
        last = next = 0
        max_len = len(nums) - 1
        while next < max_len:
            last, next = next, max(i + nums[i] for i in range(last, next + 1))
            if last == next:
                return False
        return True

    def canJump2(self, nums):
        """
        只需要判断能否到达
        每次记录当前能到达的最远距离
        如果之前的最远距离为0（即到达当前位置）且当前位置也为0，则失败
        """
        steps = 1
        for v in nums[:-1]:
            steps -= 1
            if v == steps == 0:
                return False
            steps = max(steps, v)
        return True


s = Solution()
print(s.canJump2([3, 5, 0, 0, 0]))
print(s.canJump2([0, 1]))
