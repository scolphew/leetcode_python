from base.LinkedList import ListNode


class Solution(object):
    def insertionSortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next:
            return head

        q, head.next, end = head.next, None, head

        new = ListNode(0)
        new.next = head
        while q:
            if q.val > end.val:
                end.next, q.next, q, end = q, None, q.next, q
                continue
            pre, p = new, new.next
            while p and p.val < q.val:
                pre, p = p, p.next
            if not p:
                end = q
            pre.next, q.next, q = q, p, q.next
        return new.next


if __name__ == '__main__':
    s = Solution()
    i = [6, 7, 8, 9, 1, 2]
    head = ListNode(i)
    print(s.insertionSortList(head))
