class TreeNode(object):
    """二叉树"""

    def __init__(self, x=[]):
        self.left = None
        self.right = None
        if not x:
            self.val = None
        elif type(x) is int:
            self.val = x
        elif type(x) is list:
            self.__init_with_list(x)

    def __init_with_list(self, x):
        """当输入的数据为列表时的操作"""
        from collections import deque
        node_stream = deque((self,))
        for i in x:
            node = node_stream.popleft()
            node.val = i
            if not node:
                continue
            node.left, node.right = TreeNode(None), TreeNode(None)
            node_stream.extend((node.left, node.right))

    def __repr__(self):
        ans, level = [], [self]
        while level:
            ans.extend([node.val if node else None for node in level])
            level = [kid for n in level if n for kid in (n.left, n.right)]
        while not ans[-1]:
            ans.pop()
        return str(ans)

    def __bool__(self):
        return bool(self.val)


if __name__ == '__main__':
    root = TreeNode([1, 2, 4, None, 3, None, 5, None, 6])
    # root.left = TreeNode(2)
    # root.right = TreeNode(3)
    # root.right.right = TreeNode(4)
    # root.right.right.right = TreeNode(5)
    print(root)
