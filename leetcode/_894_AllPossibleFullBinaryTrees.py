from typing import Optional

from base import TreeNode


class Solution:
    def allPossibleFBT(self, n: int) -> list[Optional[TreeNode]]:  # noqa
        d = {
            0: [],
            1: [TreeNode(0)],
        }

        def foo(num):
            if num not in d:
                ans = []
                for l_child_num in range(num):
                    r_child_num = num - 1 - l_child_num
                    for l_child in foo(l_child_num):
                        for r_child in foo(r_child_num):
                            root = TreeNode(0)
                            root.left, root.right = l_child, r_child
                            ans.append(root)
                d[num] = ans
            return d[num]

        foo(n)
        return d[n]


if __name__ == "__main__":
    s = Solution()
    y = s.allPossibleFBT(7)
    print(y)
