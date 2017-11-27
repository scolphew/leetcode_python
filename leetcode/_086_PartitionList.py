from base.LinkedList import ListNode


class Solution(object):
    def partition(self, head, x):
        """
        划分链表，
        小于x的在前面，大于等于的放后面
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        """
        head_1 = p1 = None
        head_2 = p2 = None
        p = head
        while p:
            if p.val < x:
                if p1:
                    p1.next = p
                    p1 = p
                else:
                    head_1 = p1 = p
            else:
                if p2:
                    p2.next = p
                    p2 = p
                else:
                    head_2 = p2 = p
            p = p.next
        if p1:
            p1.next = head_2
            if p2:
                p2.next = None
            return head_1
        else:
            return head_2


if __name__ == '__main__':
    s = Solution()
    a = [5, 4, 3, 2, 1, 3, 3, 3]
    print(s.partition(ListNode(a), 4))
