from base import TreeNode


class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> list[int]:  # noqa
        parents = {}
        ans = []

        def build_tree(node: TreeNode):
            if node.left:
                parents[node.left.val] = node
                build_tree(node.left)

            if node.right:
                parents[node.right.val] = node
                build_tree(node.right)

        build_tree(root)

        def dps(node: TreeNode, from_: TreeNode = None, depth: int = 0):
            if node is None:
                return
            if depth == k:
                ans.append(node.val)
                return
            if node.left != from_:
                dps(node.left, node, depth + 1)
            if node.right != from_:
                dps(node.right, node, depth + 1)
            if (p := parents.get(node.val, None)) != from_:
                dps(p, node, depth + 1)

        dps(target)
        return ans


if __name__ == "__main__":
    s = Solution()
    x = TreeNode([3, 5, 1, 6, 2, 0, 8, None, None, 7, 4])
    y = s.distanceK(x, x.left, 2)
    print(y)
