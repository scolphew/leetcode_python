from base.Tree import TreeNode


class Solution(object):
    def buildTree(self, preorder: list, inorder: list):
        """
        给出先序和中序， 求树
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """

        def build(start1, start2, length):
            if not length:
                return None
            root_val = preorder[start1]
            root = TreeNode(root_val)
            if length == 1:
                return root
            root_index = inorder.index(root_val)
            left_length = root_index - start2
            right_length = length - left_length - 1

            root.left = build(start1 + 1, start2, left_length)
            root.right = build(start1 + 1 + left_length,
                               start2 + 1 + left_length, right_length)

            return root

        return build(0, 0, len(preorder))


if __name__ == '__main__':
    s = Solution()
    p = [1, 2, 4, 5, 3, 6, 7]
    i = [4, 2, 5, 1, 6, 3, 7]
    p = [1,2]
    i = [2,1]
    print(s.buildTree(p, i))
