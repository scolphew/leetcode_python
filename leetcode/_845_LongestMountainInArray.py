from typing import List


class Solution:
    def longestMountain(self, arr: List[int]) -> int:  # noqa
        if (n := len(arr)) < 3:
            return 0
        ans = 0
        i = 1
        n1 = n - 1
        while i < n1:
            if arr[i - 1] < arr[i]:  # 刚开始需要是上升的
                start = i - 1  # 开始位置
                while i < n1 and arr[i] < arr[i + 1]:  # 持续上升
                    i += 1
                # 此时i在山巅
                if i < n1 and arr[i] > arr[i + 1]:  # 开始下降
                    i += 1
                    while i < n1 and arr[i] > arr[i + 1]:  # 持续下降
                        i += 1
                    ans = max(ans, i - start + 1)
            i += 1
        return ans


if __name__ == '__main__':
    s = Solution()
    x = s.longestMountain([0, 2, 2])
    print(x)
