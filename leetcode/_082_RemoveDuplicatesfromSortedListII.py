from base.LinkedList import ListNode


class Solution(object):
    def deleteDuplicates(self, head):
        """
        链表去重（有重复的全部删除，一个不留）
        1->2->3->3->4->4->5 --》  1->2->5.
        1->1->1->2->3 --》 2->3.
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next:
            return head
        p = head
        target = head.val
        flag = False
        per = None
        while p.next:
            if p.next.val == target:
                flag = True
            else:
                if flag:
                    if not per:
                        head = p.next
                    else:
                        per.next = p.next
                    flag = False
                else:
                    per = p
                target = p.next.val
            p = p.next
        else:
            if flag:
                if not per:
                    head = p.next
                else:
                    per.next = p.next
        return head


s = Solution()
a = ListNode([1, 1, 1, 1,3])
a = s.deleteDuplicates(a)
print(a)
