def a(begin, n_len, m):
    n = len(str(begin))
    if n_len == n:
        return 1
    if n_len < n:
        return 0
    diff = n_len - n
    _min = begin * 10 ** diff
    _max = _min + 10 ** diff - 1

    ans = int('1' * diff)
    if _max < m:
        ans = ans * 10 + 1
    elif _min < m:
        ans += m - _min + 1
    return ans


def b(m, n, s=0):
    len_num = len(str(m))
    for i in range(0, 10):
        i = s * 10 + i
        if i == 0:
            continue
        num = a(i, len_num, m)
        if num >= n:
            if n == 1:
                return i
            return b(m, n - 1, s=i)
        else:
            n -= num


# c = 123456
# for i in range(1, c + 1):
#     print(b(c, i))
if __name__ == '__main__':
    print(b(1567582787715753216, 1567582787715753216))
