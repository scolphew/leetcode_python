class Solution:
    def judgePoint24(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        from operator import add, sub, mul, truediv

        def op(a, b):
            s = set()
            s.add(a + b)
            s.add(a - b)
            s.add(b - a)
            s.add(a * b)
            if a: s.add(b / a)
            if b: s.add(a / b)
            return s

        def judge(A):
            N = len(A)
            if N == 0:
                return False
            if N == 1:
                return abs(A[0] - 24) < 10e-6

            for i in range(N):
                for j in range(N):
                    if i != j:
                        B = [A[k] for k in range(N) if i != k != j]
                        for ans in op(A[i], A[j]):
                            if judge(B + [ans]):
                                return True
                return False

        return judge(nums)


if __name__ == '__main__':
    s = Solution()
    print(s.judgePoint24([1, 2, 1, 2]))
