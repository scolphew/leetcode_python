from base.tree import TreeNode


class Solution(object):
    def buildTree(self, inorder, postorder):
        """
        中序+后续==>树
        :type inorder: List[int]
        :type postorder: List[int]
        :rtype: TreeNode
        """

        def build(start1, end2, length):
            if not length:
                return None
            root_val = postorder[end2]
            root = TreeNode(root_val)
            if length == 1:
                return root
            root_index = inorder.index(root_val)
            left_length = root_index - start1
            right_length = length - left_length - 1

            root.left = build(start1, end2 - right_length - 1, left_length)
            root.right = build(start1 + 1 + left_length, end2 - 1,
                               right_length)

            return root

        l = len(inorder)
        return build(0, l - 1, l)


if __name__ == '__main__':
    s = Solution()
    a = [4, 2, 5, 1, 6, 3, 7]
    b = [4, 5, 2, 6, 7, 3, 1]
    print(s.buildTree(a, b))
