import math
from operator import add
from typing import Optional, TypeVar
from collections.abc import Iterable
from .red_black_tree import TreeMap, TreeMapNode

__all__ = ['TreeNode', 'TreeMap', 'TreeMapNode', 'SegmentTreeNode', 'SegmentTree']

T = TypeVar('T')


class TreeNode(object):
    """二叉树"""

    def __new__(cls, x: Optional[T | Iterable] = None, *args, **kwargs):
        if x is None:
            return None
        if hasattr(x, "__iter__") and len(x) == 0:
            return None
        return super().__new__(cls, *args, **kwargs)

    def __init__(self, x: T | Iterable = None):
        self.left: Optional[TreeNode] = None
        self.right: Optional[TreeNode] = None
        if hasattr(x, "__iter__"):
            self.__init_with_iter(list(x))
        else:
            self.val = x

    def __init_with_iter(self, x: list):
        """当输入的数据为列表时的操作"""
        from collections import deque
        self.val = x[0]
        node_stream = deque((self,))
        index, length = 1, len(x)
        while index + 1 < length:
            node = node_stream.popleft()
            while not node:
                node = node_stream.popleft()
            node.left = TreeNode(x[index])
            node.right = TreeNode(x[index + 1])
            if node.left:
                node_stream.append(node.left)
            if node.right:
                node_stream.append(node.right)
            index += 2
        else:
            if index < length:
                node = node_stream.popleft()
                node.left = TreeNode(x[index])

    def get_val(self):
        return self.val

    def __repr__(self):
        ans, level = [], [self]
        while level:
            ans.extend([node.get_val() if node else None for node in level])
            level = [kid for n in level if n for kid in (n.left, n.right)]
        while ans[-1] is None:
            ans.pop()
        return str(ans)


class SegmentTreeNode(object):
    def __init__(self, start, end, val):
        """
        线段树结点
        :param start: 区间开始
        :param end: 区间结束
        :param val: 对应的值
        """
        self.start = start
        self.end = end
        self.val = val
        self.l_child: SegmentTreeNode = None
        self.r_child: SegmentTreeNode = None

    def __repr__(self):
        return f"[{self.start},{self.end},{self.val}]"


class SegmentTree(object):
    """线段树"""

    def __init__(self, nums, func=max, base=-math.inf, change_val=None,
                 desc=""):
        """
        线段树,初始化，复杂度 O(n)
        :param func: 两个区间合并后值的变化函数
                        如区间和，func为add，求最大值，func为max
        :param base: 基数，如果是add=0，max=-inf...,使得func(base,x)=x
        :param desc: 线段类型描述
        """
        self.func = func
        self.desc = desc
        self.nums = nums
        self.base = base
        self.change_val = change_val
        self.root = self._init_helper(0, len(nums) - 1)

    def _init_helper(self, start, end):
        if start > end:
            return None
        root = SegmentTreeNode(start, end, self.change_val(
            self.nums[start]) if self.change_val else self.nums[start])
        if start == end:
            return root
        mid = (start + end) >> 1
        root.l_child = self._init_helper(start, mid)
        root.r_child = self._init_helper(mid + 1, end)
        root.val = self.func(root.l_child.val, root.r_child.val)
        return root

    def __repr__(self):
        return "\n".join(self.graph())

    def graph(self, x=False, prefix=0):
        if x is False:
            x = self.root

        if x:
            yield from self.graph(x.r_child, prefix + 8)
            yield f"{' ' * prefix}{x}"
            yield from self.graph(x.l_child, prefix + 8)

    def query(self, start, end, root=False):
        """查询，复杂度O(log(n))"""
        if root is False:
            root = self.root
        if start <= root.start and end >= root.end:
            return root.val

        mid = (root.start + root.end) >> 1
        ans = self.base
        if mid >= start:
            ans = self.func(ans, self.query(start, end, root.l_child))
        if mid + 1 <= end:
            ans = self.func(ans, self.query(start, end, root.r_child))
        return ans

    def modify(self, index, value, root=False):
        if root is False:
            root = self.root
        self.nums[index] = value
        if root.start == root.end == index:
            root.val = self.change_val(value) if self.change_val else value
            return
        mid = (root.start + root.end) >> 1
        if index <= mid:
            self.modify(index, value, root.l_child)
            root.val = self.func(root.l_child.val, root.r_child.val)
        else:
            self.modify(index, value, root.r_child)
            root.val = self.func(root.l_child.val, root.r_child.val)


if __name__ == '__main__':
    # st = SegmentTree([1, 4, 3, 4, 5, 12, 12], func=mul, base=1, desc="区间和")
    st = SegmentTree([0, None, 2, 3], func=add,
                     change_val=lambda a: 0 if a is None else 1, base=0,
                     desc="区间和")

    # print(st.query(2, 3))
    st.modify(3, None)
    print(st)
    print(st.query(2, 3))

    # data = RedBlackTree.create_nodes([(i, i) for i in range(6)])
    # rb_tree = RedBlackTree(data)
    # print(rb_tree)
    # print(rb_tree.force_search(2))
    # print(rb_tree)

    # root = TreeNode([1, 2, 4, None, 3, None, 5, None, 6])
    # root.left = TreeNode(2)
    # root.right = TreeNode(3)
    # root.right.right = TreeNode(4)
    # root.right.right.right = TreeNode(5)
    # print(root)
