class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        n = len(citations)
        l, r = 0, n - 1
        while l <= r:
            mid = (l + r) / 2
            if citations[mid] >= n - mid:
                r = mid - 1
            else:
                l = mid + 1
        return n - l


if __name__ == '__main__':
    print(Solution().hIndex([1, 2, 3, 9]))
    print(Solution().hIndex([0]))
