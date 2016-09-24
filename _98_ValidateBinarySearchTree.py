from Tree import TreeNode

null = None


class Solution(object):
    def isValidBST(self, root):
        """
        判断一个树是否为二叉搜索树

        :type root: TreeNode
        :rtype: bool
        """
        if root is None:
            return True

        p = root
        stack = []
        per = float('-inf')

        while len(stack) > 0 or p is not None:
            while p is not None:
                stack.append(p)
                p = p.left
            if len(stack) > 0:
                p = stack.pop()
                if p.val <= per:
                    return False
                per = p.val
                p = p.right
        return True


if __name__ == '__main__':
    s = Solution()
    print(s.isValidBST(TreeNode([2, 1, 4, null, null, 3, 5])))
