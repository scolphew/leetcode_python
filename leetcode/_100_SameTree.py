from base.Tree import TreeNode


class Solution(object):
    def isSameTree(self, p, q):
        """
        给定两颗二叉树，判断他们是否相等
        结构相等，节点相等

        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        if p is None and q is None:
            return True
        if p is None or q is None:
            return False
        return p.val == q.val and self.isSameTree(p.left,
                                                  q.left) and self.isSameTree(
            p.right, q.right)


if __name__ == '__main__':
    p = TreeNode(0)
    q = TreeNode(0)
    s = Solution()
    print(s.isSameTree(p, q))
