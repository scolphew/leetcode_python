class Solution(object):
    def search(self, nums, target):
        """
        在一个被数组中搜索target(nums有重复)(对比033)
        :type nums: List[int]
        :type target: int
        :rtype: bool
        """

        def search(left=0, right=len(nums) - 1):
            while left <= right:
                mid = (left + right) >> 1
                if nums[mid] == target or nums[left] == target \
                        or nums[right] == target:
                    return True
                # 左半边有序
                if nums[left] == nums[right] == nums[mid]:
                    return search(left + 1, mid - 1) or search(mid + 1,
                                                               right - 1)
                if nums[mid] >= nums[left]:
                    # tag在左半边
                    if nums[left] > target or nums[mid] <= target:
                        left = mid + 1
                    else:
                        right = mid - 1
                # 右半边有序
                else:
                    # tag在右半边
                    if nums[right] < target or nums[mid] >= target:
                        right = mid - 1
                    else:
                        left = mid + 1
            return False

        return search()


if __name__ == '__main__':
    s = Solution()
    print(s.search([1, 3, 1, 1, 1], 3))
