from base.Tree import TreeNode


class Solution(object):
    def findFrequentTreeSum(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        from collections import defaultdict
        d = defaultdict(int)
        self.max_time = 0

        def foo(tree: TreeNode):
            if not tree:
                return 0
            l = foo(tree.left)
            r = foo(tree.right)
            val = tree.val + l + r
            d[val] += 1
            if d[val] > self.max_time:
                self.max_time = d[val]
            return val

        foo(root)

        return [i for i, j in d.items() if j == self.max_time]


if __name__ == '__main__':
    s = Solution()
    print(s.findFrequentTreeSum(TreeNode([5, 2, -3])))
