class Solution(object):
    def canPlaceFlowers(self, flowerbed, n):
        """
        假设你有一个很长的花坛，一部分地块种植了花，另一部分却没有。
        可是，花卉不能种植在相邻的地块上，它们会争夺水源，两者都会死去。

        给定一个花坛（表示为一个数组包含0和1，其中0表示没种植花，1表示种植了花），
        和一个数 n 。能否在不打破种植规则的情况下种入 n 朵花？
        能则返回True，不能则返回False。
        :type flowerbed: List[int]
        :type n: int
        :rtype: bool
        """
        count = 1
        max_ = 0
        for i in flowerbed:
            if i:
                # 连续count个，因为两边都是1，则只能放入一办（偶数需要减一）
                # 10001 100001 均为两个
                # 若是开头的一部分，则因为count初始值1(相当于在最开始加上1)
                # 0-001 0-0001 均为1个
                max_ += (count - 1) // 2
                count = 0
            else:
                count += 1
        else:
            # 最后一部分，只有左边是1，则
            # 100 1000 均为1
            max_ += count // 2
        return n <= max_


if __name__ == '__main__':
    s = Solution()
    print(s.canPlaceFlowers([0, 0, 0, 0], 4))
    print(s.canPlaceFlowers([0, 0, 1, 0], 4))
    print(s.canPlaceFlowers([0, 0, 1, 0, 0, 1, 0], 4))
