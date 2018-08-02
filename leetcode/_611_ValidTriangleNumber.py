class Solution(object):
    def triangleNumber(self, nums: list):
        """
        给定一个包含非负整数的数组，你的任务是统计其中可以组成三角形三条边的三元组个数。
        :type nums: List[int]
        :rtype: int
        """
        nums.sort(reverse=True)
        ans = 0
        n = len(nums)
        for i in range(n - 2):
            j, k = i + 1, n - 1
            while j < k:
                if nums[j] + nums[k] > nums[i]:
                    print(nums[i],nums[j],nums[k])
                    ans += k - j
                    j += 1
                else:
                    k -= 1
        return ans


if __name__ == '__main__':
    s = Solution()
    print(s.triangleNumber([1, 2, 3, 4, 5, 6, 7]))
