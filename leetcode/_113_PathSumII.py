from base.tree import TreeNode


class Solution(object):
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: List[List[int]]
        """
        res = []
        if not root:
            return res
        sum -= root.val
        if not root.left and not root.right:
            if sum == 0:
                return [[root.val]]
            else:
                return []
        if root.left:
            res += self.pathSum(root.left, sum)
        if root.right:
            res += self.pathSum(root.right, sum)

        return [[root.val] + i for i in res]


if __name__ == '__main__':
    s = Solution()
    root = TreeNode([5, 4, 8, 11, None, 13, 4, 7, 2, None, None, 5, 1])
    # print(root.left.left.left.left)
    # root = TreeNode(22, 0, 0)
    print(s.pathSum(root, 22))

    # print(root)
