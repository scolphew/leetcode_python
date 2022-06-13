from base.tree import TreeNode


class Solution(object):
    def hasPathSum(self, root, sum):
        """
        求是否有 跟到叶子结点的路径和为sum 的路径
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        if not root:
            return False
        sum -= root.val
        if not root.left and not root.right and not sum:
            return True
        return self.hasPathSum(root.left, sum) or self.hasPathSum(root.right,
                                                                  sum)

    def f2(self, root, sum):
        stack = [root]
        while stack and root:
            cur = stack.pop()
            if not cur.left and not cur.right and cur.val == sum:
                return True
            if cur.right:
                cur.right.val += cur.val
                stack.append(cur.right)
            if cur.left:
                cur.left.val += cur.val
                stack.append(cur.left)
        return False


if __name__ == '__main__':
    s = Solution()
    root = TreeNode([5, 4, 8, 11, None, 13, 4, 7, 2, None, 1])
    root = TreeNode([1, 2])
    print(s.hasPathSum(root, 3))
