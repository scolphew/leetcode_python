from base.tree import TreeNode


class Solution(object):
    def findMode(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return []
        stack = []
        p = root

        ans = []
        max_count = 0
        cur_count = 0
        pro_val = None
        while p or stack:
            while p:
                stack.append(p)
                p = p.left

            p = stack.pop()
            if pro_val and p.val == pro_val.val:
                cur_count += 1
            else:
                cur_count = 1
                pro_val = p

            if cur_count == max_count:
                ans.append(p.val)
            elif cur_count > max_count:
                ans = [p.val]
                max_count = cur_count
            p = p.right
        return ans


if __name__ == '__main__':
    s = Solution()
    print(s.findMode(TreeNode([2, 1, 3, 1])))
    print(s.findMode(TreeNode([1, None, 2])))
    print(s.findMode(TreeNode([2, 1])))
    print(s.findMode(TreeNode([1, 2, 3])))
    print(s.findMode(TreeNode([2, 2, 3])))
    print(s.findMode(TreeNode([1, None, 2, 2])))
