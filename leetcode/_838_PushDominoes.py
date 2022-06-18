class Solution:
    def pushDominoes(self, dominoes: str) -> str:  # noqa
        st = list(dominoes)
        n, i = len(st), 0
        f = 0
        while i < n:
            if st[i] == 'R':
                f = 1
            elif f and st[i] == '.':
                st[i] = f
                f += 1
            elif st[i] == 'L':
                f = 0
            i += 1
        i = n - 1
        f = 0
        while i >= 0:
            if st[i] == 'L':
                f = 1
            elif st[i] == 'R':
                f = 0
            else:
                if f:  # 受到向左的力
                    if st[i] == '.':
                        st[i] = 'L'
                    else:
                        tmp = st[i]
                        if tmp > f:
                            st[i] = 'L'
                        elif tmp < f:
                            st[i] = 'R'
                        else:
                            st[i] = '.'
                    f += 1
                else:  # 没有向左的力
                    if st[i] != '.':
                        st[i] = "R"

            i -= 1
        return "".join(st)


if __name__ == '__main__':
    s = Solution()
    l = [
        "LLR",
        "...L",
        "R...L",
        "...L...R...",
        "RR.L",
        ".L.R...LR..L..",
    ]
    for e in l:
        x = s.pushDominoes(e)
        print(e, "===", x)
