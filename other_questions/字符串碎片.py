#!/usr/bin/env python
# -*- encoding: utf-8 -*-
if __name__ == '__main__':
    s = input()
    if s:
        lst = []
        p = None
        c = 0
        for i in s:
            if p == i:
                c += 1
            else:
                lst.append(c)
                p = i
                c = 1
        else:
            lst.append(c)
        ans = lst[1:]
        ans = sum(lst) / len(ans)
        print("%.2f" % round(ans, 2))
    else:
        print(0)
