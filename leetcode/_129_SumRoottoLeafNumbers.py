from base.tree import TreeNode


class Solution(object):
    def sumNumbers(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        p = root
        stack = []
        tmp, res = 0, 0
        pre = None
        while p or stack:
            if p:
                if not p.left and not p.right:  # 叶子
                    res += tmp * 10 + p.val
                    pre = p
                    p = None
                else:
                    stack.append(p)
                    tmp = tmp * 10 + p.val
                    p = p.left if p.left else p.right  # 向下
            else:
                top = stack[-1]
                if pre is top.left:  # 如果上一次是左孩子
                    if top.right:
                        p = top.right
                    else:
                        p = None
                        pre = stack.pop()
                        tmp //= 10
                else:
                    pre = stack.pop()
                    tmp //= 10
        return res


if __name__ == '__main__':
    s = Solution()
    print(s.sumNumbers(TreeNode([1, 2, 3, 4, 5, 6, 7])))
    print(s.sumNumbers(TreeNode([1, 2, 3])))
    print(s.sumNumbers(TreeNode([1])))
    # root = TreeNode([1, 2, 3, 4])
    print(s.sumNumbers(TreeNode([1, 2, 3, 4])))
    print(s.sumNumbers(TreeNode([1, 2, 3, None, 4, None, 5])))
