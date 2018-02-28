class Solution(object):
    def validSquare(self, p1, p2, p3, p4):
        """
        :type p1: List[int]
        :type p2: List[int]
        :type p3: List[int]
        :type p4: List[int]
        :rtype: bool
        """
        A, B, C, D = sorted([p1, p2, p3, p4])
        AD = A[0] - D[0], A[1] - D[1]
        BC = B[0] - C[0], B[1] - C[1]

        AB = A[0] - B[0], A[1] - B[1]
        AC = A[0] - C[0], A[1] - C[1]

        print(A, B, C, D)
        print(AD, BC)

        # AD=BC
        # AD⊥BC
        # AB=AC
        return AD[0] != 0 and \
               BC[1] != 0 and \
               AD[0] ** 2 + AD[1] ** 2 == BC[0] ** 2 + BC[1] ** 2 and \
               AD[0] * BC[0] + AD[1] * BC[1] == 0 and \
               AB[0] ** 2 + AB[1] ** 2 == AC[0] ** 2 + AC[1] ** 2

    def valid_square(self, p1, p2, p3, p4):
        p = [p1, p2, p3, p4]
        dist = {}
        for i in range(1, 4):
            for j in range(i):
                tmp = (p[i][0] - p[j][0]) ** 2 + (p[i][1] - p[j][1]) ** 2
                dist[tmp] = dist.get(tmp, 0) + 1
        return len(dist) == 2 and 2 in dist.values() and 4 in dist.values()


if __name__ == '__main__':
    s = Solution()
    print(s.validSquare([0, 0],
                        [1, 1],
                        [1, 0],
                        [0, 1], ))
    print(s.validSquare([0, 1],
                        [2, 1],
                        [1, 0],
                        [1, 2], ))
