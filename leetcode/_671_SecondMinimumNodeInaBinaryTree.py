from base.Tree import TreeNode


class Solution:
    def findSecondMinimumValue(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        from queue import Queue
        a, b = root.val, 0x7fffffff
        q = Queue()
        q.put(root)
        while not q.empty():
            x: TreeNode = q.get()
            if a < x.val < b:
                b = x.val
            elif x.val == a:
                q.put(x.left)
                q.put(x.right)

        return -1 if b == 0x7fffffff else b
