from base.Tree import TreeNode


class Solution(object):
    def findBottomLeftValue(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        from collections import deque
        q1 = deque()
        q2 = deque()
        q1.append(root)
        while q1:
            ans = q1[0]
            while q1:
                node = q1.popleft()
                if node.left:
                    q2.append(node.left)
                if node.right:
                    q2.append(node.right)
            q1 = q2
            q2 = deque()
        return ans.val


if __name__ == '__main__':
    s = Solution()
    print(s.findBottomLeftValue(TreeNode([3, 1, 5, 0, 2, 4, 6])))
