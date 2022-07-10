from base import TreeNode


class Solution:
    def subtreeWithAllDeepest(self, root: TreeNode) -> TreeNode:  # noqa
        def dfs(node: TreeNode = root) -> tuple[int, TreeNode | None]:
            if not node:
                return 0, None
            left_depth, left_ans = dfs(node.left)
            right_depth, right_ans = dfs(node.right)
            if left_depth > right_depth:
                return left_depth + 1, left_ans
            elif left_depth < right_depth:
                return right_depth + 1, right_ans
            else:
                return left_depth + 1, node

        return dfs()[1]


if __name__ == "__main__":
    s = Solution()
    y = s.subtreeWithAllDeepest(TreeNode([3, 5, 1, 6, 2, 0, 8, None, None, 7, 4]))
    print(y)
