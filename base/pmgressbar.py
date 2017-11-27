#!/usr/bin/env python
# -*- encoding: utf-8 -*-

import sys
from collections import Iterable


class ProgressBar(Iterable):
    def __init__(self, data, n=None, desc=None, length=20):
        """
        简易进度条
        :param iter: 迭代器
        :param n: 总数
        :param desc: 描述
        """
        self.iter = data
        if n is None:
            try:
                self.n = len(data)
            except TypeError:
                self.n = None
        else:
            self.n = n
        self.desc = desc if desc else '进度'
        self.length = length

    def __iter1(self):
        index = 0
        for each in self.iter:
            index += 1
            left = (self.desc + ":" if self.desc else "") + "|"
            len_1, len_2 = divmod(int(self.length * 8 * index / self.n), 8)
            s_1 = chr(0x2588) * len_1
            s_2 = chr(0x2590 - len_2) if len_2 else ''
            s_3 = ' ' * (self.length - len_1 - len(s_2))
            right = "|【{}/{}】".format(index, self.n)
            sys.stderr.write("\r" + left + s_1 + s_2 + s_3 + right)
            # sys.stderr.flush()
            yield each
        sys.stderr.write("\n")

    def __iter2(self):
        index = 0
        for each in self.iter:
            index += 1
            sys.stderr.write('\r{}:{}'.format(self.desc, index))
            # sys.stderr.flush()
            yield each
        sys.stderr.write("\n")

    def __iter__(self):
        if self.n:
            return self.__iter1()
        else:
            return self.__iter2()


if __name__ == '__main__':
    s = 0
    for i in ProgressBar(range(10000)):
        s += 1
        import time
        time.sleep(0.01)
    print(s)
