from base.Tree import TreeNode


class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []
        from collections import deque
        lst = deque()
        lst.append(root)
        result = []
        first = root
        flag = False
        while lst:
            node = lst.popleft()
            if node == first:
                flag = True
                current_level = []
                current_level.append(node.val)
                result.append(current_level)
            else:
                current_level.append(node.val)

            if node.left:
                if flag:
                    first = node.left
                    flag = False
                lst.append(node.left)
            if node.right:
                if flag:
                    first = node.right
                    flag = False
                lst.append(node.right)
        return result


if __name__ == '__main__':
    null = None
    root = TreeNode([3, 9, 20, null, null, 15, 7])
    s = Solution()
    print(s.levelOrder(root))
