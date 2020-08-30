class Solution(object):
    def isIdealPermutation(self, A):
        """
        :type A: List[int]
        :rtype: bool
        """
        n = len(A)
        max_ = -1
        for i in range(1, n):
            if A[i] < max_:
                return False
            max_ = max(max_, A[i - 1])
        return True

    def doo2(self, A):
        for i in range(len(A)):
            if A[i] == i - 1 or A[i] == i + 1 or A[i] == i:
                continue
            return False
        return True




if __name__ == '__main__':
    s = Solution()
    print(s.isIdealPermutation([0]))
    print(s.isIdealPermutation([1, 2, 0]))
    print(s.isIdealPermutation([0, 1, 2]))
    print(s.isIdealPermutation([2, 0, 1]))
    print(s.isIdealPermutation([2, 1, 0]))

    print(s.doo2([0]))