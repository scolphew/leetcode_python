class Solution(object):
    def hIndex(self, citations):
        """
        标出数组中大于x的书有x个的最大x
        :type citations: List[int]
        :rtype: int
        """
        citations.sort(reverse=True)
        # if not citations or not citations[0]:
        # return 0
        for i, j in enumerate(citations, 1):
            # print(i,j)
            if i > j:
                return i - 1
        return i

    def f2(self, citations):
        length = len(citations)
        count = [0] * (length + 1)

        for i in citations:
            if i > length:
                count[length] += 1
            else:
                count[i] += 1
        print(citations, count)
        res = 0
        for i in range(length, -1, -1):
            res += count[i]
            if res >= i:
                return i
        return 0


if __name__ == '__main__':
    s = Solution()
    print(s.f2([0]))
    print(s.f2([0, 0, 0, 0]))
    print(s.f2([4, 4, 0, 0]))
    print(s.f2([1, 2, 3]))
    print(s.f2([1, 2, 0]))
    print(s.f2([100]))
    print(s.f2([1, 2]))
    print(s.f2([11, 15]))
