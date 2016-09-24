class ListNode(object):
    def __init__(self, nums):
        if type(nums) is int:
            self.val = nums
            self.next = None
            return
        if len(nums) == 0:
            self = None
            return

        if len(nums) == 1:
            self.val = nums[0]
            self.next = None
            return

        self.val = nums[0]
        per = self
        for i in nums[1:]:
            x = ListNode(i)
            per.next = x
            per = x

    def __str__(self):
        result = []
        per = self
        while per is not None:
            result.append(per.val)
            per = per.next
        return str(result)


if __name__ == '__main__':
    print(ListNode([1, 2, 3]))