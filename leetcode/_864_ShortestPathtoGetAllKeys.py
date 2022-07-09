import collections
import heapq


class Solution:
    def shortestPathAllKeys(self, grid: list[str]) -> int:
        R, C = len(grid), len(grid[0])  # noqa

        # @aA = (i,j)
        location = {v: (r, c)
                    for r, row in enumerate(grid)
                    for c, v in enumerate(row)
                    if v not in '.#'}

        def neighbors(r, c):
            for cr, cc in ((r - 1, c), (r, c - 1), (r + 1, c), (r, c + 1)):
                if 0 <= cr < R and 0 <= cc < C:
                    yield cr, cc

        def bfs_from(source):
            r, c = location[source]
            seen = [[False] * C for _ in range(R)]
            seen[r][c] = True
            queue = collections.deque([(r, c, 0)])
            dist = {}
            while queue:
                r, c, d = queue.popleft()
                if source != grid[r][c] != '.':  # gird[r,c]!=#, 可能为 @abcdefABCDEF
                    dist[grid[r][c]] = d
                    continue  # Stop walking from here if we reach a point of interest
                for cr, cc in neighbors(r, c):
                    if grid[cr][cc] != '#' and not seen[cr][cc]:
                        seen[cr][cc] = True
                        queue.append((cr, cc, d + 1))
            return dist

        dists = {place: bfs_from(place) for place in location}  # 距离
        target_state = 2 ** sum(p.islower() for p in location) - 1  # 对应所有钥匙全拿到的状态

        # Dijkstra 不需要开锁 只要拿到钥匙
        pq = [(0, '@', 0)]  # 距离，符号，状态(获取钥匙的状态)
        final_dist = collections.defaultdict(lambda: float('inf'))  # <符号, 状态> -> 步数
        final_dist['@', 0] = 0
        while pq:
            d, place, state = heapq.heappop(pq)
            if final_dist[place, state] < d:
                continue
            if state == target_state: return d
            for destination, d2 in dists[place].items():
                state2 = state
                if destination.islower():  # key
                    state2 |= (1 << (ord(destination) - ord('a')))
                elif destination.isupper():  # lock
                    if not (state & (1 << (ord(destination) - ord('A')))):  # no key
                        continue

                if d + d2 < final_dist[destination, state2]:
                    final_dist[destination, state2] = d + d2
                    heapq.heappush(pq, (d + d2, destination, state2))

        return -1
