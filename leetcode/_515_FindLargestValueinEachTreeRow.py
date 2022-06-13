from base.tree import TreeNode


class Solution(object):
    def largestValues(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return []
        from collections import deque
        MIN = -0xffffffff
        q1 = deque()
        q2 = deque()
        q1.append(root)
        ans = []
        while q1:
            max_val = MIN
            while q1:
                node = q1.popleft()
                if node.val > max_val:
                    max_val = node.val
                if node.left:
                    q2.append(node.left)
                if node.right:
                    q2.append(node.right)
            q1 = q2
            q2 = deque()
            ans.append(max_val)
        return ans


if __name__ == '__main__':
    s = Solution()
    print(s.largestValues(TreeNode([1, 3, 2, 5, 3, None, 9])))
    print(s.largestValues(TreeNode([1])))
    print(s.largestValues(TreeNode([])))
