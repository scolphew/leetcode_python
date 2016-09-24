class TreeNode(object):
    def __init__(self, x):
        if type(x) is int:
            self.val = x
            self.left = None
            self.right = None
            return

        if type(x) is list:
            self.val = x[0]
            return

        return None
