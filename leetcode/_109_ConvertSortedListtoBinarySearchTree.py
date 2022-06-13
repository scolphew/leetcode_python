from base.tree import TreeNode
from base.LinkedList import ListNode


class Solution(object):
    def sortedListToBST(self, head):
        """
        升序链表，转二叉搜索树
        :type head: ListNode
        :rtype: TreeNode
        """
        if not head:
            return
        if not head.next:
            return TreeNode(head.val)
        slow, fast = head, head.next.next
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        tmp = slow.next
        slow.next = None
        root = TreeNode(tmp.val)
        root.left = self.sortedListToBST(head)
        root.right = self.sortedListToBST(tmp.next)
        return root


if __name__ == '__main__':
    s = Solution()
    i = [1, 2, 3, 4, 5]
    print(s.sortedListToBST(ListNode(i)))
