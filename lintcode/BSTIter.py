# from ..base.Tree import TreeNode
class BSTIterator:
    # @param root: The root of binary tree.
    def __init__(self, root):
        self.stack = []
        self.curt = root

    # @return: True if there has next node, or false
    def hasNext(self):
        return self.curt is not None or len(self.stack) > 0

    # @return: return next node
    def next(self):
        while self.curt is not None:
            self.stack.append(self.curt)
            self.curt = self.curt.left

        self.curt = self.stack.pop()
        nxt = self.curt
        self.curt = self.curt.right
        return nxt


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None

    def __str__(self):
        return str(self.val)


if __name__ == "__main__":
    r = TreeNode(1)
    r.right = TreeNode(2)
    r.right.right = TreeNode(3)
    r.right.right.right = TreeNode(4)
    s = BSTIterator(r)
    while s.hasNext():
        print(s.next())
