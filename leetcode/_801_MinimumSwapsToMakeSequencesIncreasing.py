from typing import List


class Solution:
    def minSwap(self, nums1: List[int], nums2: List[int]) -> int:  # noqa
        no_swap, swap = 0, 1
        for i in range(1, len(nums1)):
            if nums1[i - 1] >= nums2[i] or nums2[i - 1] >= nums1[i]:  # 之前交换的，也必须交换
                swap += 1
            elif nums1[i - 1] >= nums1[i] or nums2[i - 1] >= nums2[i]:  # 之前没有交换的，必须交换
                swap, no_swap = no_swap + 1, swap
            else:  # 两个数组前一位都比两个当前为小
                tmp = min(swap, no_swap)
                swap, no_swap = tmp + 1, tmp
        return min(swap, no_swap)


if __name__ == '__main__':
    s = Solution()
    print(s.minSwap([0, 3, 5, 8, 9], [2, 1, 4, 6, 9]))
