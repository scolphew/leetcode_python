class NumArray(object):
    @staticmethod
    def lowbit(a):
        return a & -a

    def add(self, i, val):
        """将第i个数加上x"""
        while i <= self.n:
            self.c[i] += val
            i += self.lowbit(i)

    def __init__(self, nums):
        """
        树状数组
        一个数组，交叉执行下列两个函数：
        1. 修改数组的第x位
        2. 求i，j闭区间的和
        """
        self.n = len(nums)
        self.a, self.c = nums, [0] * (self.n + 1)

        for i in range(self.n):
            self.add(i + 1, nums[i])

    def update(self, i, val):
        """将第i个数改为x，相当于将第i个数加上(val-nums[i])"""
        diff = val - self.a[i]
        self.a[i] = val
        self.add(i + 1, diff)

    def sum(self, i):
        """求前i个数的值"""
        res = 0
        while i > 0:
            res += self.c[i]
            i -= self.lowbit(i)
        return res

    def sum_range(self, i, j):
        """求l到r的值，闭区间"""
        return self.sum(j + 1) - self.sum(i)


if __name__ == '__main__':
    nums = [1, 3, 5]  # len = 17

    s = NumArray(nums)

    print(s.sum_range(0, 2))

    s.update(1, 2)

    print(s.sum_range(0, 2))
