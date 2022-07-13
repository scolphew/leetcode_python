class Solution:
    def advantageCount(self, nums1: list[int], nums2: list[int]) -> list[int]:  # noqa
        n = len(nums1)
        a = sorted(nums1)
        b = sorted(enumerate(nums2), key=lambda x: x[1])
        i, j = 0, 0
        ans = [-1] * n
        x = []
        while i < n and j < n:
            if a[i] <= b[j][1]:
                x.append(a[i])
            else:
                ans[b[j][0]] = a[i]
                j += 1
            i += 1
        i, j = 0, 0
        while i < n and j < n:
            if ans[i] == -1:
                ans[i] = x[j]
                j += 1
            i += 1
        return ans


if __name__ == "__main__":
    s = Solution()
    y = s.advantageCount([12, 24, 8, 32], nums2=[13, 25, 32, 11])
    print(y)
