from typing import Optional

from base import TreeNode


class Solution:
    def pruneTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:  # noqa
        p: Optional[TreeNode] = root
        pre: Optional[TreeNode] = None
        stack: list[TreeNode] = []

        while p or stack:
            while p:
                stack.append(p)
                p = p.left
            p = stack[-1]
            if p.right and p.right != pre:
                stack.append(p.right)
                p = p.right.left
            else:
                stack.pop()
                if not (p.left or p.right or p.val):
                    # 应该删除
                    if stack:
                        parent = stack[-1]
                        if p == parent.left:
                            parent.left = None
                        else:
                            parent.right = None
                    else:
                        root = None
                pre, p = p, None
        return root


if __name__ == '__main__':
    s = Solution()
    x = s.pruneTree(TreeNode([0, None, 0, 0, 0]))
    print(x)
