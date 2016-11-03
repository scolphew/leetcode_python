from base.LinkedList import ListNode


class Solution(object):
    def reverseBetween(self, head, m, n):
        """
        倒转链表m到n之间的内容
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        """
        current = ListNode(-1)
        current.next = head
        p = current
        for i in range(m - 1):
            current = current.next
        last = current.next
        last_before_reverse = current
        par = current  # 反转部分的前一个
        current = par.next
        for _ in range(n - m + 1):
            tmp = current.next
            current.next = par
            par = current
            current = tmp
        last.next = current
        last_before_reverse.next = par
        return p.next


s = Solution()
a = ListNode([1, 2, 3, 4, 5])
print(s.reverseBetween(a, 2, 4))
