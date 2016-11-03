class TreeNode(object):
    def __init__(self, x):
        self.left = None
        self.right = None
        if type(x) is int:
            self.val = x
            return
        if type(x) is list:
            self.val = x[0]
            queue = []
            queue.append(self)
            del (x[0])

            while len(x) > 0:
                this = queue[0]
                del (queue[0])
                if this is None:
                    continue
                left = x[0]
                del (x[0])
                if left is None:
                    this.left = None
                else:
                    this.left = TreeNode(left)
                queue.append(this.left)
                if len(x) > 0:
                    right = x[0]
                    del (x[0])

                    if right is None:
                        this.right = None
                    else:
                        this.right = TreeNode(right)
                    queue.append(this.right)
        return None

    def __str__(self):
        queue = []
        lst = []
        queue.append(self)

        while len(queue) > 0:
            this = queue[0]
            lst.append(this.val if this is not None else None)
            del (queue[0])

            if this is not None:
                if this.left:
                    queue.append(this.left)
                if this.right:
                    queue.append(this.right)

        return str(lst)


if __name__ == '__main__':
    root = TreeNode([1, 2, 4, None, 3, None, 5, None, 6])
    # root.left = TreeNode(2)
    # root.right = TreeNode(3)
    # root.right.right = TreeNode(4)
    # root.right.right.right = TreeNode(5)
    print(root)
