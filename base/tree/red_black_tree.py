"""
红黑树
"""
from typing import (
    Iterator, MutableMapping, TypeVar, Callable, Generic, Optional,
    Mapping, Iterable,
)

_K = TypeVar("_K")  # KV的key
_V = TypeVar("_V")  # KV的value
_KV = tuple[_K, _V]

_Comparator = Optional[Callable[[_K, _K], int]]  # 比较函数

_RED = False
_BLACK = True


class TreeMapNode(Generic[_K, _V]):
    """
    红黑树结点定义
    """
    __slots__ = (
        "key", "value",
        "left", "right", "parent",
        "color",
    )

    def __init__(self, key: _K, value: _V, parent: 'TreeMapNode[_K,_V]|None'):
        self.key = key
        self.value = value
        self.parent: TreeMapNode[_K, _V] = parent
        self.color = _BLACK
        self.left: TreeMapNode[_K, _V] | None = None
        self.right: TreeMapNode[_K, _V] | None = None

    def set_value(self, value: _V) -> _V:
        old_value = self.value
        self.value = value
        return old_value

    def __repr__(self):
        return f"{self.key}={self.value}"


def _parent_of(p: TreeMapNode[_K, _V]):
    return p.parent if p else None


def _left_of(p: TreeMapNode[_K, _V]):
    return p.left if p else None


def _right_of(p: TreeMapNode[_K, _V]):
    return p.right if p else None


def _color_of(p: TreeMapNode[_K, _V]):
    return p.color if p else _BLACK


def _key_of(p: TreeMapNode[_K, _V]):
    return p.key if p else _BLACK


def _set_color(p: TreeMapNode[_K, _V], color: bool):
    if p:
        p.color = color


class TreeMap(MutableMapping[_K, _V]):
    """
    红黑树
    """

    def __init__(self, m: MutableMapping[_K, _V] | Mapping[_K, _V] = None, comparator: _Comparator = None):
        """
        :param m: 用于初始化的映射结构数据
        :param comparator: 用于比较两个元素大小的比较器，返回正负或零。
        """
        self._size = 0  # 元素数量
        self._comparator: _Comparator = comparator  # 比较器
        self._root: TreeMapNode[_K, _V] | None = None  # 根节点
        self._mod_count: int = 0  # 快速失败

        # 暂时不对有序输入做个数处理
        if m:
            self.update(m)

    def pop(self, __key: _K = None, default=None) -> _V:
        """
        移除 key，返回旧值。
        :param __key: K
        :param default: 默认值
        :return: 如果存在，返回旧制；否则，返回 None。
        """
        if __key:
            p = self.get_node(__key)
        else:
            p = self.first_node
        if p is None:
            return default

        old_value = p.value
        self._delete_node(p)
        return old_value

    def _left_rotate(self, x: TreeMapNode[_K, _V]):
        """
        左旋, 其中 x 的右孩子 y 不为 nil。
               x                 y
             ↙ ↘             ↙  ↘
           α      y    ->     x     γ
               ↙  ↘       ↙ ↘
             β       γ     α    β
        :param x: 结点
        """
        y = x.right

        # step 1: 调整 β 的位置(并修改其父节点)
        x.right = y.left
        if y.left is not None:
            y.left.parent = x

        # step 2.1: 修改 y 的父节点
        y.parent = x.parent
        # step 2.1: 当x为树根时，修改树根。否则修改 x 父节点对应的孩子结点为 y。
        if x.parent is None:
            self._root = y
        elif x.parent.left is x:
            x.parent.left = y
        else:
            x.parent.right = y

        # step 3: 修改 x 和 y 的父子关系
        y.left = x
        x.parent = y

    def _right_rotate(self, x: TreeMapNode[_K, _V]):
        """
        右旋, 其中 y 的右孩子 y 不为 nil。
                x                 y
              ↙ ↘             ↙  ↘
            y      γ    ->     α     x
          ↙  ↘                   ↙ ↘
         α      β                 β    γ
        :param x: 结点
        """
        y = x.left

        # step 1: 调整 β 的位置(并修改其父节点)
        x.left = y.right
        if y.right is not None:
            y.right.parent = x

        # step 2.1: 修改 y 的父节点。
        y.parent = x.parent
        # step 2.2: 当x为树根时，修改树根。否则修改x父节点对应的孩子结点为y)
        if x.parent is None:
            self._root = y
        elif x.parent.left is x:
            x.parent.left = y
        else:
            x.parent.right = y

        # step 3: 修改 y 和 y 的父子关系
        y.right = x
        x.parent = y

    def _add_node(self, k: _K, v: _V, parent: TreeMapNode[_K, _V], add_left: bool):
        """
        将 KV 插入树中
        :param k: K
        :param v: V
        :param add_left:
        :return:
        """
        z = TreeMapNode(k, v, parent)
        if add_left:
            parent.left = z
        else:
            parent.right = z
        self._insert_fixup(z)  # 调整颜色
        self._size += 1
        self._mod_count += 1

    def _insert_fixup(self, z: TreeMapNode[_K, _V]):
        """
        插入后调整颜色
        :param z: 插入的结点
        :return:
        """
        z.color = _RED  # 因为插入的是红节点，不影响黑高
        while z and z is not self._root and z.parent.color is _RED:  # z.p.c == red 带非空检查版本
            # 由于本函数最后会将根染黑，z.p=R，所以 z.p.p != None
            if _parent_of(z) is _left_of(_parent_of(_parent_of(z))):  # 判断 z 的父节点是左孩子
                y = _right_of(_parent_of(_parent_of(z)))  # 叔叔
                if _color_of(y) is _RED:  # 红叔叔
                    # 此时的情况如下(父为红->祖为黑)：
                    # 解决思路：父叔染黑，祖染红。从祖节点递归。不需要考虑 z 是左孩子还是右孩子
                    #      zppB                 zppR
                    #    zpR     yR   ->    zpB     tB
                    #   zR                 zR
                    _set_color(_parent_of(z), _BLACK)
                    _set_color(y, _BLACK)
                    _set_color(_parent_of(_parent_of(z)), _RED)
                    z = _parent_of(_parent_of(z))
                else:  # 黑叔叔
                    # 此时的情况如下(父为红->祖为黑)：z的黑高和y相同。RB后面的数字表示该节点子树的黑高。
                    # 解决思路：
                    # 如果 z 是右孩子，左旋zp(之后z变为原zp)。统一下一步方法。(初始zpp的黑高为2)
                    #       zppB                  zppB                   zppB
                    #    zpR    yB1    ->      zR    yB1 -修改指针->  zpR     yB1
                    #   a1  zR             zpR   c1                 zR  c1
                    #      b1 c1         a1  b1                    a1  b1
                    # 右旋zpp, 再将该子树的黑高调整为原始的2
                    #        zpR                    zp(R->B)
                    #   zR      zppB     ->    zpR       zpp(B->R)
                    # a1   b1   c1   yB1      a1   b1   c1   yB1
                    if z is _right_of(_parent_of(z)):
                        z = _parent_of(z)
                        self._left_rotate(z)  # 此时z为原zp
                    _set_color(_parent_of(z), _BLACK)  #
                    _set_color(_parent_of(_parent_of(z)), _RED)
                    self._right_rotate(_parent_of(_parent_of(z)))
            else:  # 判断 z 的父节点是左孩子
                y = _left_of(_parent_of(_parent_of(z)))  # 伯伯
                if _color_of(y) is _RED:  # 红伯伯
                    _set_color(_parent_of(z), _BLACK)
                    _set_color(y, _BLACK)
                    _set_color(_parent_of(_parent_of(z)), _RED)
                    z = _parent_of(_parent_of(z))
                else:  # 黑伯伯
                    if z is _left_of(_parent_of(z)):
                        z = _parent_of(z)
                        self._right_rotate(z)
                    _set_color(_parent_of(z), _BLACK)
                    _set_color(_parent_of(_parent_of(z)), _RED)
                    self._left_rotate(_parent_of(_parent_of(z)))
        # 完成之后整棵树黑高一直，将根节点染黑
        self._root.color = _BLACK

    @staticmethod
    def _successor(z: TreeMapNode[_K, _V]):
        """获得 z 的后继节点，没有则返货 None"""
        if z is None:
            return None
        elif z.right is not None:  # 右子树存在，则返回右子树最左节点
            p = z.right
            while p.left is not None:
                p = p.left
            return p
        else:  # 右子树不存在，向上递归，找到第一个不是右孩子的父节点
            p = z.parent
            ch = z
            while p is not None and ch is p.right:
                ch = p
                p = p.parent
            return p

    def _delete_node(self, p: TreeMapNode[_K, _V]) -> None:
        self._mod_count += 1
        self._size -= 1

        if p.left is not None and p.right is not None:  # 如果p有两个孩子，修改之后的p只会有右孩子
            # 用 p 的后继节点 s 代替 p，改为删除 s。（s 没有左孩子）
            s = self._successor(p)
            p.key, p.value = s.key, s.value
            p = s

        # 这里 p 最多只有一个孩子
        replacement = p.left if p.left is not None else p.right
        if replacement is not None:  # p有且只有一个孩子（p是黑的，孩子是红的）
            replacement.parent = p.parent
            if p.parent is None:  # p 是根
                self._root = replacement
            elif p is p.parent.left:  # p 是左孩子
                p.parent.left = replacement
            else:
                p.parent.right = replacement
            p.left = p.right = p.parent = None
            # 注释这 2 行，改为 replacement.color = _BLACK 代替
            # if p.color is _BLACK:  # 删除红节点不影响黑高，不需要处理
            #     self._delete_fixup(replacement) # 修改一下
            replacement.color = _BLACK
        elif p.parent is None:  # p是孤根
            self._root = None
        else:  # p 是叶子节点
            if p.color is _BLACK:
                self._delete_fixup(p)
            # 清空指针
            if p is p.parent.left:
                p.parent.left = None
            else:
                p.parent.right = None
            p.parent = None

    def _delete_fixup(self, x: TreeMapNode[_K, _V]) -> None:
        """
        删除前调整颜色。
        :param x: 黑色节点。（叶子节点）
        :return:
        """
        # 如果 x 是红色，走最后一行直接涂黑即可。
        # 如果 x 是黑色，意味着 x 的黑高比其兄弟小1，需要将其兄弟的黑高减1
        while x is not self._root and x.color is _BLACK:
            if x is x.parent.left:  # 左孩子
                sib = x.parent.right  # 兄弟
                if _color_of(sib) is _RED:
                    # 情况 1: 红兄弟（sl sr肯定是黑色）
                    # 将父节点左旋（x指针不变），转化为234处理。(该处理红黑树的黑高不变)
                    #      xpB                    sR                 sB
                    #   xB     sR       ->   xpB      sr  -> 颜色  xpR  sr
                    #        sl  sr         xB   sl               xB sl
                    _set_color(sib, _BLACK)  # 兄弟(现在是子树跟)
                    _set_color(x.parent, _RED)
                    self._left_rotate(x.parent)
                    sib = _right_of(x.parent)
                # assert sib.color == _BLACK
                if _color_of(_left_of(sib)) is _BLACK and _color_of(_right_of(sib)) is _BLACK:
                    # 情况 2: 黑兄弟，且兄弟两个黑儿子。
                    # 直接将兄弟涂黑，该处理会导致右子树黑高减一。递归父节点。
                    _set_color(sib, _RED)
                    x = x.parent
                else:
                    # 情况3: 黑兄弟，且兄弟孩子左红又黑，将其转化为情况4处理
                    # 右旋右兄弟后，将新右兄弟和其右孩子颜色互换，转化为情况4
                    # 假设ef黑高0为，则abcd的黑高为1
                    # 处理之后，黑高不变
                    #         xpU                       xpU
                    #     xB        sB       ->     xB       sl(R->B)
                    #   a1  b1   slR   srB        a1  b1    c1   sB(B->R)
                    #           c1  d1  e  f                    d1  rbR
                    #                                               e   f
                    if _color_of(_right_of(sib)) is _BLACK:
                        _set_color(_left_of(sib), _BLACK)
                        _set_color(sib, _RED)
                        self._right_rotate(sib)
                        sib = _right_of(x.parent)
                    # 情况四: 黑兄弟，且兄弟孩子右红（左无所谓），将其转化为情况4处理
                    # 处理之后，x子树的黑高多1（删去节点之后平衡），整体黑高不变。
                    #       xpU                      s(B->U)
                    #    xB     sB        ->     xp(U->B)    sr(R->B)
                    #  a   b   c   srR         xB   c         d   e
                    #             e    f      a b
                    _set_color(sib, x.parent.color)
                    _set_color(x.parent, _BLACK)
                    _set_color(_right_of(sib), _BLACK)
                    self._left_rotate(x.parent)
                    x = self._root
            else:
                sib = x.parent.left
                if _color_of(sib) is _RED:
                    _set_color(sib, _BLACK)
                    _set_color(x.parent, _RED)
                    sib = _left_of(x.parent)
                if _color_of(_left_of(sib)) is _BLACK and _color_of(_right_of(sib)) is _BLACK:
                    _set_color(sib, _RED)
                    x = x.parent
                else:
                    if _color_of(_left_of(sib)) is _BLACK:
                        _set_color(_right_of(sib), _BLACK)
                        _set_color(sib, _RED)
                        self._left_rotate(sib)
                        sib = _left_of(x.parent)
                    _set_color(sib, x.parent.color)
                    _set_color(x.parent, _BLACK)
                    _set_color(_left_of(sib), _BLACK)
                    self._right_rotate(x.parent)
                    x = self._root
        x.color = _BLACK

    def __contains__(self, item: _K) -> bool:
        """
        item in tree
        """
        return self.get_node(item) is not None

    def contains_key(self, key: _K) -> bool:
        return key in self

    def contains_value(self, value: _V) -> bool:
        p = self.first_node
        while p:
            if value == p.value:
                return True
            p = self._successor(p)
        return False

    def __getitem__(self, item: _K) -> _V:
        """

        :param item:
        :return:
        """
        p = self.get_node(item)
        if p:
            return p.value
        raise KeyError(item)

    @property
    def comparator(self):
        return self._comparator

    @property
    def first_key(self):
        return _key_of(self.first_node)

    @property
    def last_key(self):
        return _key_of(self.last_node)

    @property
    def first_node(self) -> TreeMapNode[_K, _V] | None:
        p = self._root
        if p is not None:
            while p.left:
                p = p.left
        return p

    @property
    def last_node(self) -> TreeMapNode[_K, _V] | None:
        p = self._root
        if p:
            while p.right:
                p = p.right
        return p

    def get_node(self, key: _K) -> TreeMapNode[_K, _V] | None:
        """
        :param key: key
        :return: 红黑树结点，或者 None
        """
        p = self._root
        if self._comparator:
            while p:
                cmp = self._comparator(key, p.key)
                if cmp < 0:
                    p = p.left
                elif cmp > 0:
                    p = p.right
                else:
                    return p
        else:
            while p:
                cmp = -1 if key < p.key else 1 if key > p.key else 0
                if cmp < 0:
                    p = p.left
                elif cmp > 0:
                    p = p.right
                else:
                    return p
        return None

    def get_ceiling_node(self, key: _K) -> TreeMapNode[_K, _V] | None:
        """
        获取指定结点，不存在则返回大于的最小值
        :param key:
        :return:
        """
        p = self._root
        while p:
            cmp = self._compare(key, p.key)
            if cmp < 0:
                if p.left:
                    p = p.left
                else:
                    return p
            elif cmp > 0:
                if p.right:
                    p = p.right
                else:
                    parent = p.parent
                    ch = p
                    # 向上找到第一个是左孩子的祖先节点，返回其父节点
                    # 如果是右孩子，父节点比自己小
                    while parent and ch is parent.right:
                        ch = parent
                        parent = parent.parent
                    return parent
            else:
                return p
        return None

    def get_higher_node(self, key: _K) -> TreeMapNode[_K, _V] | None:
        """
        获取指定结点，不存在则返回大于的最小值
        :param key:
        :return:
        """
        p = self._root
        while p:
            cmp = self._compare(key, p.key)
            if cmp < 0:
                if p.left:
                    p = p.left
                else:
                    return p
            elif cmp > 0:
                if p.right:
                    p = p.right
                else:
                    parent = p.parent
                    ch = p
                    while parent and ch is parent.right:
                        ch = parent
                        parent = parent.parent
                    return parent
        return None

    def get_floor_node(self, key: _K) -> TreeMapNode[_K, _V] | None:
        """
        获取指定结点，不存在则返回小于的最大值
        :param key:
        :return:
        """
        p = self._root
        while p:
            cmp = self._compare(key, p.key)
            if cmp > 0:
                if p.right:
                    p = p.right
                else:
                    return p
            elif cmp < 0:
                if p.left:
                    p = p.left
                else:
                    parent = p.parent
                    ch = p
                    while parent and ch is parent.left:
                        ch = parent
                        parent = parent.parent
                    return parent
            else:
                return p
        return None

    def get_lower_node(self, key: _K) -> TreeMapNode[_K, _V] | None:
        """
        获取指定结点，不存在则返回小于的最大值
        :param key:
        :return:
        """
        p = self._root
        while p:
            cmp = self._compare(key, p.key)
            if cmp > 0:
                if p.right:
                    p = p.right
                else:
                    return p
            elif cmp < 0:
                if p.left:
                    p = p.left
                else:
                    parent = p.parent
                    ch = p
                    while parent and ch is parent.left:
                        ch = parent
                        parent = parent.parent
                    return parent
        return None

    def __setitem__(self, __k: _K, __v: _V):
        self.put(__k, __v)

    def _compare(self, key1: _K, key2: _V) -> int:
        if self._comparator:
            return self._comparator(key1, key2)
        else:
            return 1 if key1 > key2 else 0 if key1 == key2 else -1

    def put(self, key: _K, value: _V, replace_old: bool = True) -> _V | None:
        """
        将 <key, value> 插入树中。
        :param key: K
        :param value: V
        :param replace_old: 当 key 已经存在石，是否使用 value 替换原值。
        :return: 当 key 已存在是返回原值；否则返回 None。
        """
        x = self._root
        y = None  # parent
        cmp: int = 0

        if (cpr := self._comparator) is not None:
            while x is not None:
                y = x
                cmp = cpr(key, x.key)
                if cmp < 0:
                    x = x.left
                elif cmp > 0:
                    x = x.right
                else:  # 已存在，替换
                    old_value = x.value
                    if replace_old:
                        x.value = value
                    return old_value
        else:
            while x is not None:
                y = x
                cmp = -1 if key < x.key else 1 if key > x.key else 0
                if cmp < 0:
                    x = x.left
                elif cmp > 0:
                    x = x.right
                else:  # 已存在，替换
                    old_value = x.value
                    if replace_old:
                        x.value = value
                    return old_value
        if y is None:  # 说明此时树为空
            self._add_node_to_empty_map(key, value)
        else:
            self._add_node(key, value, y, cmp < 0)
        return None

    def put_if_absent(self, key: _K, value: _V) -> _V:
        """如果不存在则插入返回None，存在返回value，不插入"""
        return self.put(key, value, replace_old=False)

    def _add_node_to_empty_map(self, k: _K, v: _V):
        self._root = TreeMapNode(k, v, None)
        self._size += 1
        self._mod_count += 1

    def compute_if_absent(self, key: _K, mapping_function: Callable[[_K], _V]) -> _V:
        """
        当 key 不存在时调用 mapping_function,计算并插入返回，等价于
        >>> tree = TreeMap()
        >>> def foo(self_, key_):
        >>>     if key not in tree:
        >>>         tree[key] = mapping_function(key_)
        >>>     return tree[key]

        :param key:
        :param mapping_function:
        :return: 新值，存在 key 则返回 None
        """
        t = self._root
        if t is None:
            new_value = mapping_function(key)
            self._add_node_to_empty_map(key, new_value)
            return new_value

        parent = t
        cmp = 0
        while t:
            parent = t
            cmp = self._compare(key, t.key)
            if cmp < 0:
                t = t.left
            elif cmp > 0:
                t = t.right
            else:  # 存在
                return None

        # 插入新值
        new_value = mapping_function(key)
        self._add_node(key, new_value, parent, cmp < 0)
        return new_value

    def compute_if_present(self, key, remapping_function: Callable[[_K, _V], _V]) -> _V:
        """
        当 key 存在时调用 mapping_function,并将其返回值插入，等价于
        >>> tree = TreeMap()
        >>> def foo(self_, key_):
        >>>     if key in tree:
        >>>         tree[key_] = remapping_function(key_,tree[key_])
        >>>     return tree[key]

        :param key:
        :param remapping_function:
        :return:
        """
        node = self.get_node(key)
        if node:
            new_value = remapping_function(key, node.value)
            return node.set_value(new_value)
        return None

    def compute(self, key: _K, remapping_function: Callable[[_K, _V], _V]) -> _V:
        """
        key 不存在，计算插入新值，返回新值
        key 存在 计算新值插入新值，返回新值
        :param key:
        :param remapping_function:
        :return:
        """
        t = self._root
        if t is None:
            new_value = remapping_function(key, None)
            self._add_node_to_empty_map(key, new_value)
            return new_value

        cmp = 0
        parent = None
        while t:
            parent = t
            cmp = self._compare(key, t.key)
            if cmp < 0:
                t = t.left
            elif cmp > 0:
                t = t.right
            else:
                new_value = remapping_function(key, t.value)
                return t.set_value(new_value)
        new_value = remapping_function(key, None)
        self._add_node(key, new_value, parent, cmp < 0)
        return new_value

    def update(self, __m: Iterable[_KV], **kwargs: dict[_K, _V]) -> None:
        for k, v in __m:
            self.put(k, v)
        for k, v in kwargs:
            self.put(k, v)

    def __delitem__(self, __v: _K) -> None:
        self.pop(__v)

    def clear(self) -> None:
        self._mod_count += 1
        self._size = 0
        self._root = None

    def __copy__(self):
        # todo
        pass

    def __len__(self) -> int:
        return self._size

    def __iter__(self) -> Iterator[_K]:
        def foo():
            for k, _ in self.items():
                yield k

        return foo()

    def keys(self) -> list[_K]:
        key_set = []
        for k in self:
            key_set.append(k)
        return key_set

    def items(self) -> Iterator[_KV]:
        def foo():
            t = self.first_node
            while t:
                yield t.key, t.value
                t = self._successor(t)

        return foo()

    def values(self) -> list[_V]:
        values = []
        for _, v in self.items():
            values.append(v)
        return values
