from base import TreeNode


class Solution:
    def searchBST(self, root, val):
        """
        :type root: TreeNode
        :type val: int
        :rtype: TreeNode
        """
        while root or root.val != val:
            if root.val > val:
                root = root.left
            else:
                root = root.right
        return root
