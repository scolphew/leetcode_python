class Solution(object):
    def jump(self, nums):
        """
        当前索引表示最大的跳数，求到达终点的最小跳数
        每一次挑选下一步能调的最远的地方
        :type nums: List[int]
        :rtype: int
        """
        step = last = next = 0
        while next < len(nums) - 1:
            step += 1
            last, next = next, max(i + nums[i] for i in range(last, next + 1))
        return step

    def jump2(self, nums):
        step = current = 0
        while current < len(nums) - 1:
            if current + nums[current] >= len(nums) - 1:
                step += 1
                break
            else:
                next = current + 1
                nextNext = current + 2
                jumpDist = nums[current]
                for i in range(1, jumpDist + 1):
                    temp = nums[current + i] + (current + i)
                    if temp > nextNext:
                        nextNext = temp
                        next = current + i
                current = next
                step += 1
        return step


s = Solution()
print(s.jump([2, 3, 1, 1, 4]))
print(s.jump2([2, 3, 1, 1, 4]))
