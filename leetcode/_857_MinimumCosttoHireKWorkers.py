from typing import List
import heapq


class Solution:
    def mincostToHireWorkers(self, quality: List[int], wage: List[int], k: int) -> float:  # noqa
        # 因为对质量没有要求，所以追求性价比高的，但同时要成本低。
        # 性价比超高但价格也非常高的不能选
        lst = sorted([(w / q, q) for q, w in zip(quality, wage)])  # q/w 性价比, 按性价比到序排序
        print(lst)

        l = []  # 价格负数的堆
        for wq, q in lst[:k]:
            l.append(-q)
        heapq.heapify(l)
        qualities = -sum(l)  # 质量
        ans = qualities * wq  # 选性价比最高的k个人

        for wq, q in lst[k:]:
            # 弹出最贵的（q最大，-q最小），换位当前
            max_q = -heapq.heappushpop(l, -q)
            qualities -= max_q - q
            ans = min(ans, wq * qualities)
        return ans


if __name__ == '__main__':
    s = Solution()
    y = s.mincostToHireWorkers([10, 20, 5], wage=[70, 50, 30], k=2)
    print(y)
