from base.tree import TreeNode


class Solution(object):
    def flatten(self, root):
        """
        把二叉树按照先序摊平，每个节点边做其先序前一节点的右孩子
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """

        def find_last(root):
            tmp = root
            while tmp.right or tmp.left:
                if tmp.right:
                    tmp = tmp.right
                elif tmp.left:
                    tmp = tmp.left
            return tmp

        tmp = root
        while tmp:
            # print(tmp.val)
            if tmp.left:
                left_last = find_last(tmp.left)
                left_last.right = tmp.right
                tmp.right = tmp.left
                tmp.left = None
            tmp = tmp.right


if __name__ == '__main__':
    s = Solution()
    root = TreeNode([1, 2, 3, 4, 5, 6, 7])
    s.flatten(root)
    print(root)
