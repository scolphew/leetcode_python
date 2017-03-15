from base.Tree import TreeNode


class BinaryTree(TreeNode):
    def __init__(self, num):
        super().__init__(num)
        self.count = 0
        self.rep = 0

    def add(self, num):
        if num == self.val:
            self.count += 1
            self.rep += 1
            return self.count - self.rep

        elif num < self.val:
            if self.left:
                self.count += 1
                return self.left.add(num)
            else:
                self.count += 1
                self.left = BinaryTree(num)
                return 0
        else:
            if self.right:
                return self.count + 1 + self.right.add(num)
            else:
                self.right = BinaryTree(num)
                return self.count + 1

    def get_val(self):
        return self.val, self.count, self.rep


class Solution(object):
    def countSmaller(self, nums):
        """
        统计数组中i之后比i小的数量
        :type nums: List[int]
        :rtype: List[int]
        """
        if not nums:
            return []
        length = len(nums)
        res = [0] * length
        root = BinaryTree(nums[-1])
        for i, j in enumerate(nums[-2::-1], 2):
            res[-i] = root.add(j)
        print(root)
        return res


def p(s: Solution, input, output):
    o = s.countSmaller(input)
    s = []
    for a, b in zip(o, output):
        if a == b:
            s.append(a)
        else:
            s.append((a, b))
    print(input, s, o == output)


if __name__ == '__main__':
    s = Solution()
    p(s, [5, 2, 6, 1], [2, 1, 1, 0])

    i = [1, 2, 3, 4, 5, 8, 7, 6, 5, 32, 6, 2, 7, 2, 6, 2, 7, 2, 7, 9, 3, 23,
         54, 9]
    o = [0, 0, 4, 5, 5, 13, 9, 6, 5, 13, 5, 0, 5, 0, 3, 0, 2, 0, 1, 1, 0, 1, 1,
         0]

    # p(s, i, o)

    # print(TreeNode([1, 2, 3, None, 4, 5]))
