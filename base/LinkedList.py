class ListNode(object):
    def __new__(cls, x=None, *args, **kwargs):
        if x is None:
            return None
        if hasattr(x, "__iter__") and len(x) == 0:
            return None
        return super().__new__(cls, *args, **kwargs)

    def __init__(self, x=None, *args):
        if hasattr(x, "__iter__"):
            self.__init_with_iter(x)
        else:
            self.val = x
            self.next = None

    def __bool__(self):
        return self is not None

    def __len__(self):
        p = self.next
        res = 1
        while p is not None:
            res += 1
            p = p.next
        return res

    def __init_with_iter(self, x):
        self.val = x[0]
        self.next = None
        tmp = self
        for i in x[1:]:
            tmp.next = ListNode(i)
            tmp = tmp.next

    def __str__(self):
        return str(self.val) + "," + str(self.next)
        # result, per = [], self
        # while per:
        #     result.append(per.val)
        #     per = per.next
        # return str(result)


if __name__ == '__main__':
    print(ListNode([1]))
