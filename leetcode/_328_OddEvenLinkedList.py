from base.LinkedList import ListNode


class Solution(object):
    def oddEvenList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        dummy1 = odd = ListNode(0)
        dummy2 = even = ListNode(0)
        while head and head.next:
            odd.next = head
            odd = odd.next
            even.next = odd.next
            even = even.next
            head = even.next
        if head:
            odd.next = head
            odd = odd.next
            even.next = None
        odd.next = dummy2.next
        return dummy1.next


if __name__ == '__main__':
    s = Solution()
    for i in range(10):
        i = [j for j in range(i)]
        print(s.oddEvenList(ListNode(i)))

