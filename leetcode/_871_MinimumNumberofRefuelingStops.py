import heapq


class Solution:
    def minRefuelStops(self, target: int, startFuel: int, stations: list[list[int]]) -> int:  # noqa
        n = len(stations)
        ans = 0
        fuel, prev_site = startFuel, 0
        pq = []
        for i in range(n + 1):
            site = stations[i][0] if i < n else target  # 位置
            fuel -= site - prev_site  # 汽油剩余
            while fuel < 0 and pq:  # 需要加油 且 可以加油 时 加油
                fuel -= heapq.heappop(pq)
                ans += 1
            if fuel < 0:
                return -1
            if i < n:
                heapq.heappush(pq, -stations[i][1])
                prev_site = site
        return ans


if __name__ == "__main__":
    s = Solution()
    y = s.minRefuelStops(100, startFuel=10, stations=[[10, 60], [20, 30], [30, 30], [60, 40]])
    print(y)
