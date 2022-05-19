from typing import TypeVar, Iterable, Optional, Generic

T = TypeVar("T")


class ListNode(Generic[T]):
    def __new__(cls, x: T | Iterable[T] = None, iter_input=True, *args, **kwargs):
        if x is None:
            return None
        if hasattr(x, "__iter__") and iter_input:
            try:
                next(iter(x))
            except StopIteration:
                return None
        return super().__new__(cls, *args, **kwargs)

    def __init__(self, x: T | Iterable[T] = None, iter_input: bool = True, *args):
        if hasattr(x, "__iter__") and iter_input:
            self.__init_with_iter(x)
        else:
            self.val: T = x
            self.next: Optional[ListNode[T]] = None

    def __bool__(self) -> bool:
        return self is not None

    # def __len__(self) -> int:
    #     p = self.next
    #     res = 1
    #     while p is not None:
    #         res += 1
    #         p = p.next
    #     return res

    def __init_with_iter(self, x: Iterable[T]) -> None:
        iter_ = iter(x)
        self.val: T = next(iter_)
        self.next: Optional[ListNode[T]] = None
        tmp = self
        for i in iter_:
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
