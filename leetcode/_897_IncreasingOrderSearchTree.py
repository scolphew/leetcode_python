from base import TreeNode


class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:  # noqa
        p = TreeNode(-1)
        pre = p

        def foo(r: TreeNode):
            nonlocal pre
            if r is None:
                return

            foo(r.left)

            pre.right = r
            r.left = None
            pre = r

            foo(r.right)

        foo(root)
        return p.right


if __name__ == "__main__":
    s = Solution()
    y = s.increasingBST(TreeNode([4, 2, 6, 1, 3, 5, 7]))
    print(y)
