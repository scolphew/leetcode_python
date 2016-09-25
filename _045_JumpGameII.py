class Solution(object):
    def jump(self, nums):
        """
        当前索引表示最大的跳数，求到达终点的最小跳数

        :type nums: List[int]
        :rtype: int
        """
        length = len(nums)
        if length < 2:
            return 0
        if length == 2:
            return 1
        curIn = length - 1 # 剩余的长度（当前终点）（每次向前移动终点）
        steps = 0 # 跳跃次数
        while curIn > 0:
            i = 0 # 每次从0开始
            while i < curIn:
                # 如果当前位置能跳到重点当前终点则前进一步
                # 或者说把终点向前移动
                if nums[i] >= curIn - i:
                    steps += 1
                    curIn = i
                i += 1
        return steps


s = Solution()
print(s.jump([2, 3, 1, 1, 4]))
