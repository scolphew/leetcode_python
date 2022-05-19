from typing import Optional, List

from base import ListNode


class Solution:
    def numComponents(self, head: Optional[ListNode], nums: List[int]) -> int:  # noqa
        nums_set = set(nums)
        cur = head
        ans = 0
        while cur:
            if cur.val in nums_set and (cur.next is None or cur.next.val not in nums_set):
                ans += 1
            cur = cur.next

        return ans


if __name__ == '__main__':
    s = Solution()
    print(s.numComponents(ListNode([0, 1, 2, 3, 4]), [0, 1, 3, 4]))
