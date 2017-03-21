import math
from operator import add, mul


class TreeNode(object):
    """二叉树"""

    def __new__(cls, x=None, *args, **kwargs):
        if x is None:
            return None
        if hasattr(x, "__iter__") and len(x) == 0:
            return None
        return super().__new__(cls, *args, **kwargs)

    def __init__(self, x=None):
        self.left = None
        self.right = None
        if hasattr(x, "__iter__"):
            self.__init_with_iter(x)
        else:
            self.val = x

    def __init_with_iter(self, x):
        """当输入的数据为列表时的操作"""
        from collections import deque
        self.val = x[0]
        node_stream = deque((self,))
        index, lengrh = 1, len(x)
        while index + 1 < lengrh:
            node = node_stream.popleft()
            while not node:
                node = node_stream.popleft()
            node.left = TreeNode(x[index])
            node.right = TreeNode(x[index + 1])
            node_stream.append(node.left)
            node_stream.append(node.right)
            index += 2
        else:
            if index < lengrh:
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


BLACK = "BLACK"
RED = "RED"
VC = '│'
HC = '─'
SIZE = 3
RIG = '┌' + HC * SIZE
LEF = '└' + HC * SIZE
SP = '  '
IND1 = SP * (SIZE + 1)
IND2 = VC + SP * SIZE


class RBNode(object):
    def __init__(self, key=None, value=None, color=BLACK):
        """红黑树结点"""
        self.key = key
        self.value = value
        self.color = color
        self.left = None
        self.right = None
        self.p = None

    def __repr__(self):
        return f"{self.key}{'◆' if self.color is BLACK else '◇'}{self.value}"


class RedBlackTree(object):
    @staticmethod
    def create_nodes(data_list):
        if not isinstance(data_list[0], tuple):
            data_list = [(key, None) for key in data_list]
        for k, v in data_list:
            yield k, v

    def __init__(self, data=False, default_val=0):
        """红黑树"""
        self.nil = RBNode()
        self.root = self.nil
        self.default_val = default_val
        if hasattr(data, "__iter__"):
            for key, val in data:
                self.insert(RBNode(key, val))

    def __repr__(self):
        return "\n".join(self.graph())

    def graph(self, x=False, prefix=""):
        """输出子树"""
        if x is False:
            x = self.root
        if x is not self.nil:
            p = x.p
            last_prefix = ''
            if p is not self.nil:
                pp = p.p
                last_prefix = LEF if p.left is x else RIG
                if pp is not self.nil:
                    if (pp.left is p) is (p.left is x):
                        prefix += IND1
                    else:
                        prefix += IND2
            yield from self.graph(x.right, prefix)
            yield f"{prefix}{last_prefix}{x}"
            yield from self.graph(x.left, prefix)

    def insert(self, z: RBNode):
        """插入结点z"""
        y = self.nil  # x的父结点
        x = self.root
        while x is not self.nil:
            y = x
            if z.key < x.key:
                x = x.left
            else:
                x = x.right

        if y is self.nil:
            """如果原本是空树，则插入的z为树根"""
            self.root = z
        elif z.key < y.key:
            y.left = z
        else:
            y.right = z
        z.p = y
        z.left = self.nil
        z.right = self.nil
        z.color = RED
        self._insert_fix_up(z)

    def delete(self, z):
        y = z
        y_original_color = y.color
        if z.left is self.nil:  # 左孩子为叶节点， 用右孩子代替自己
            x = z.right
            self._transplant(z, x)
        elif z.right is self.nil:  # 右孩子为叶节点，用左孩子代替自己
            x = z.left
            self._transplant(z, x)
        else:  # 有两个孩子
            y = self.minimum(z.right)  # 获的z的最小值y(注意：y没有左孩子)
            y_original_color = y.color
            x = y.right
            # if y.p is z:  # y就是z的右孩子,直接y的右孩子代替y（y没有左孩子）
            #     x.p = y
            if y.p is not z:  # y非x的孩子，用x代替y，把y放到z的位置
                # 不是右孩子，替换的时候要先把z的右子树给y，用y的右子树代替y
                self._transplant(y, x)
                y.right = z.right
                y.right.p = y

            self._transplant(z, y)  # 用y代替z
            y.left = z.left  # z一定右左孩子
            y.left.p = y
            y.color = z.color
        if y_original_color is BLACK:
            self._delete_fix_up(x)

    def is_empty(self):
        return self.root is self.nil

    def search(self, key, x=False):
        """
        在结点x（默认为树根）的子树上搜索key
        :return:
        """
        if x is False:
            x = self.root
        while x is not self.nil and key != x.key:
            if key < x.key:
                x = x.left
            else:
                x = x.right
        return x

    def right_walk(self, x=False):
        if x is False:
            x = self.root
        if x is not self.nil:
            yield from self.right_walk(x.right)
            yield x
            yield from self.right_walk(x.left)

    def left_walk(self, x=False):
        if x is False:
            x = self.root
        if x is not self.nil:
            yield from self.left_walk(x.left)
            yield x
            yield from self.left_walk(x.right)

    def force_search(self, key):
        """搜索key=key的结点并返回，如果没有，则插入该key，val为默认值"""
        y = self.nil
        x = self.root
        while x is not self.nil:
            if key == x.key:
                return x
            y = x
            if key < x.key:
                x = x.left
            else:
                x = x.right
        z = RBNode()
        original_z = z
        z.value = self.default_val
        z.key = key
        z.p = y
        if y is self.nil:
            self.root = z
        elif z.key < y.key:
            y.left = z
        else:
            y.right = z
        z.left = self.nil
        z.right = self.nil
        z.color = RED
        self._insert_fix_up(z)
        return original_z

    def maximum(self, x=False):
        """返回x的子孙中值最大的结点"""
        if x is False:
            x = self.root
        while x.left is not self.nil:
            x = x.right
        return x

    def minimum(self, x=False):
        """返回x的子孙中值最小的结点"""
        if x is False:
            x = self.root
        while x.left is not self.nil:
            x = x.left
        return x

    def successor(self, x):
        """后继结点，返回大于x的最小结点"""
        if x.right is not self.nil:
            return self.minimum(x.right)
        y = x.p
        while y is not self.nil and x is y.right:
            x = y
            y = y.p
        return y

    def predecessor(self, x):
        """后继结点，返回大于x的最小结点"""
        if x.left is not self.nil:
            return self.maximum(x.left)
        y = x.p
        while y is not self.nil and x is y.left:
            x = y
            y = y.p
        return y

    def _left_rotate(self, x):
        """
        左旋
              x                y
             ↙ ↘             ↙  ↘
           α    y    →     x    γ
               ↙  ↘       ↙  ↘
             β    γ    α   β
        """
        y = x.right  # 先获得y

        x.right = y.left  # 移动β
        if y.left is not self.nil:  # β父节点
            y.left.p = x

        # 调整父结点
        y.p = x.p
        if x.p is self.nil:
            """x为根节点"""
            self.root = y
        else:
            if x is x.p.left:
                x.p.left = y
            else:
                x.p.right = y

        # x调整为y的左孩子
        y.left = x
        x.p = y

    def _right_rotate(self, x):
        """
        右旋
              x              y
             ↙ ↘           ↙  ↘
            y   γ  →     α    x
          ↙  ↘                ↙  ↘
        α    β             β    γ
        """
        y = x.left  # 先获得y

        # 移动β
        x.left = y.right
        if y.right is not self.nil:
            y.right.p = x

        # 调整父节点
        if x.p is self.nil:
            """x为根节点"""
            self.root = y
        else:
            if x is x.p.left:
                x.p.left = y
            else:
                x.p.right = y

        # x调整为y的有孩子
        y.right = x
        x.p = y

    def _insert_fix_up(self, z):
        """插入调整，插入的z.color=RED"""
        while z.p.color is RED:
            if z.p is z.p.p.left:  # 父亲是左孩子
                y = z.p.p.right  # 叔叔
                if y.color is RED:  # 红叔叔
                    # 染色 父节点，叔叔，祖父
                    z.p.color = BLACK
                    y.color = BLACK
                    z.p.p.color = RED
                    z = z.p.p
                else:  # 黑叔叔
                    if z is z.p.right:
                        # z为右孩子，就把他变为左孩子
                        z = z.p
                        self._left_rotate(z)

                    # 染色 祖父右移
                    z.p.color = BLACK
                    z.p.p.color = RED
                    self._right_rotate(z.p.p)
            else:
                # 父亲是右孩子
                y = z.p.p.left  # 伯伯
                if y.color is RED:  # 红伯伯
                    # 染色 父节点，叔叔，祖父
                    z.p.color = BLACK
                    y.color = BLACK
                    z.p.p.color = RED
                    z = z.p.p
                else:
                    if z is z.p.left:
                        z = z.p
                        self._right_rotate(z)

                    z.p.color = BLACK
                    z.p.p.color = RED
                    self._left_rotate(z.p.p)
        self.root.color = BLACK

    def _delete_fix_up(self, x):
        while x is not self.root and x.color is BLACK:  # 黑色非根
            if x is x.p.left:  # x是左孩子
                w = x.p.right  # 弟弟
                if w.color is RED:  # 红弟弟, 把他变成黑弟弟,左移父节点
                    w.color = BLACK
                    x.p.color = RED
                    self._left_rotate(x.p)
                    w = x.p.right
                if w.left.color is BLACK and w.right.color is BLACK:
                    # 两个黑侄子,上色 向上一层
                    w.color = RED
                    x = x.p
                else:
                    if w.right.color is BLACK:  # 否则，右边是黑色的
                        w.left.color = BLACK  # 左边染黑
                        w.color = RED
                        self._right_rotate(w)
                        w = x.p.right
                    w.color = w.p.color
                    w.p.color = BLACK
                    self._left_rotate(x.p)
                    x = self.root
            else:  # x 是右孩子
                w = x.p.left  # 哥哥
                if w.color is RED:
                    w.color = BLACK
                    x.p.color = RED
                    self._right_rotate(x.p)
                    w = x.p.left
                if w.left.color is BLACK and w.right.color is BLACK:
                    w.color = RED
                    x = x.p
                else:
                    if w.left.color is BLACK:
                        w.right.color = BLACK
                        w.color = RED
                        self._left_rotate(w)
                        w = x.p.left
                    w.color = w.p.color
                    w.p.color = RED
                    self._right_rotate(x.p)
                    x = self.root
        x.color = BLACK

    def _transplant(self, u, v):
        """
        用v代替u,只改变父节点的关系
        """
        if u.p is self.nil:
            self.root = v
        elif u is u.p.left:
            u.p.left = v
        else:
            u.p.right = v
        v.p = u.p


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
            yield f"{' '*prefix}{x}"
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
