from LinkedList import ListNode


class Solution(object):
    def rotateRight(self, head, k):
        """
        在倒数第k个位置旋转链表
        :example
            head = ListNode([1, 2, 3, 4, 5])
            k = 2
            rotateRight(head, k)->[4, 5, 1, 2, 3]

        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if head is None or k == 0:
            return head
        p = head
        length = 0
        index = 0
        while index < k and p is not None:
            length += 1
            p = p.next
            index += 1
        # k > length
        if p is None:
            k = k % length
            if k == 0:
                return head
            index = 0
            p = head
            while index < k and p is not None:
                p = p.next
                index += 1
        q = head
        while p.next is not None:
            q = q.next
            p = p.next
        p.next = head
        result = q.next
        q.next = None
        return result


s = Solution()
for i in range(9):
    root = ListNode([1, 2, 3])
    print(s.rotateRight(root, i))
