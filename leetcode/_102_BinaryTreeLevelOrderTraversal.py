from base.tree import TreeNode


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

    def soluion3(self, root):
        ans, level = [], [root]
        while root and level:
            ans.append([node.val for node in level])
            level = [kid for n in level for kid in (n.left, n.right) if kid]
        return ans


if __name__ == '__main__':
    null = None
    root = TreeNode([3, 9, 20, null, null, 15, 7])
    # root = TreeNode([])
    s = Solution()
    print(s.soluion3(root))
