from base.LinkedList import ListNode


class Solution(object):
    def sortList2(self, head):
        """
        超时
        :type head: ListNode
        :rtype: ListNode
        """

        def sort(head):
            if head.next is None:
                return None
            if head.next.next is None:
                return head.next
            left = ListNode(0)
            right = ListNode(0)
            l, r = left, right
            tmp = head.next.val
            p = head.next.next
            while p is not None:
                if p.val < tmp:
                    q = p.next
                    l.next = p
                    l = p
                    p = q
                    l.next = None
                else:
                    q = p.next
                    r.next = p
                    r = p
                    p = q
                    r.next = None
            t = sort(left)
            s = sort(right)
            mid = head.next
            if t is not None:
                t.next = mid
                mid.next = right.next
                head.next = left.next
            else:
                mid.next = right.next
            if s is not None:
                return s
            else:
                return mid

        h = ListNode(0)
        h.next = head
        sort(h)
        return h.next

    def sortList(self, head):
        """链表排序 要求O(nlogn)O(1) 归并"""

        def merge(h1, h2):
            dummy = tail = ListNode(0)
            while h1 and h2:
                if h1.val < h2.val:
                    tail.next, tail, h1 = h1, h1, h1.next
                else:
                    tail.next, tail, h2 = h2, h2, h2.next

            tail.next = h1 or h2
            return dummy.next

        if not head or not head.next:
            return head

        slow, fast = head, head
        pre = None
        while fast and fast.next:
            pre, slow, fast = slow, slow.next, fast.next.next
        pre.next = None
        head = self.sortList(head)
        slow = self.sortList(slow)
        return merge(head, slow)


if __name__ == '__main__':
    # s = Solution()
    # print(s.sortList(ListNode([4, 3, 2, 1])))
    s = Solution()
    i = [5, 1, 2, 7, 8]
    print(i)
    r = ListNode(i)
    r = s.sortList(r)
    print(len(i), len(r))
