from typing import List
from collections import defaultdict, Counter
from operator import add, sub, mul


class Polynomial:
    """
    一个多项式
    可能是
    1： 一个数字
    2： 一个变量
    3： 数字乘以变量（单项式）
    5： 多项式
    """

    def __init__(self, val=None, type_=0) -> None:
        self.d = defaultdict(int)
        if type_ == 1:
            self.d[()] = int(val)
        elif type_ == 2:
            self.d[(val,)] = 1

    def __add__(self, other: defaultdict):
        for k, v in other.d.items():
            self.d[k] += v
        return self

    def __sub__(self, other: defaultdict):
        for k, v in other.d.items():
            self.d[k] -= v
        return self

    def __mul__(self, other: defaultdict):
        ans = Polynomial()
        for k1, v1 in self.d.items():
            for k2, v2 in other.d.items():
                ans.d[tuple(sorted(k1 + k2))] += v1 * v2
        return ans

    def to_list(self):
        return ["{0}{1}{2}".format(v, "*" if k else "", "*".join(k), k)
                for k, v in
                sorted(self.d.items(), key=lambda x: (-len(x[0]), x[0], x[1]))
                if v]

    def calculate(self, map_: defaultdict):
        for k, v in self.d.copy().items():
            l = list(k)
            flag = False
            for each in k:
                if each in map_:
                    flag = True
                    l.remove(each)
                    v *= map_[each]
            if flag:
                self.d[tuple(sorted(l))] += v
                self.d[k] = 0
        return self

    def __str__(self):
        return str(self.to_list())

    def __repr__(self):
        return self.__str__()


class Solution:
    def basicCalculatorIV(self, expression: str, evalvars: List[str],
                          evalints: List[int]) -> List[str]:

        def num(start, f, t, type_):
            # 变量，将变量存入element
            j = start
            while j + 1 < n and f <= expression[j + 1] <= t:
                j += 1
            int_element = expression[start:j + 1]
            # 构建多项式,并入栈
            int_polynomial = Polynomial(int_element, type_)
            polynomial_stack.append(int_polynomial)
            # 返回索引
            return j

        def calculate():
            while op_stack and op_stack[-1] != '(':
                b = polynomial_stack.pop()
                a = polynomial_stack.pop()
                c = op_stack.pop()(a, b)
                polynomial_stack.append(c)

        # 变量表
        map_ = {k: v for k, v in zip(evalvars, evalints)}

        n = len(expression)
        op_stack = []
        polynomial_stack = []

        i = 0
        while i < n:
            element = expression[i]
            if element == '(':
                op_stack.append(element)
            elif 'a' <= element <= 'z':
                i = num(i, 'a', 'z', 2)
            elif '0' <= element <= '9':
                i = num(i, '0', '9', 1)
            elif element == ')':
                # 向前计算，直到左括号
                while op_stack and op_stack[-1] != '(':
                    polynomial = polynomial_stack.pop()
                    tmp_polynomial = polynomial_stack.pop()
                    tmp_op = op_stack.pop()
                    tmp_polynomial = tmp_op(tmp_polynomial, polynomial)
                    polynomial_stack.append(tmp_polynomial)
                else:
                    if op_stack.pop() != "(":
                        print("error")
                        return
            elif element == '+':
                calculate()
                op_stack.append(add)
            elif element == '-':
                calculate()
                op_stack.append(sub)
            elif element == '*':
                op_stack.append(mul)
            else:
                pass
            i += 1
        else:
            while op_stack:
                polynomial = polynomial_stack.pop()
                tmp_polynomial = polynomial_stack.pop()
                tmp_op = op_stack.pop()
                tmp_polynomial = tmp_op(tmp_polynomial, polynomial)
                polynomial_stack.append(tmp_polynomial)
        return polynomial_stack[-1].calculate(map_).to_list()


if __name__ == '__main__':
    s = Solution()
    print(s.basicCalculatorIV("e + 8 - a + 5", ["e"], [1]))
    print(
        s.basicCalculatorIV("e - 8 + temperature - pressure",
                            ["e", "temperature"],
                            [1, 12]))
    print(s.basicCalculatorIV("(e + 8) * (e - 8)", [], []))
    print(s.basicCalculatorIV("7-7", [], []))
    print(s.basicCalculatorIV("a * b * c + b * a * c * 4", [], []))
    print(s.basicCalculatorIV(
        "((a - b) * (b - c) + (c - a)) * ((a - b) + (b - c) * (c - a))", [],
        []))
    print(s.basicCalculatorIV("a * a", ["a"], [-7]))
