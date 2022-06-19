from typing import List


class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:  # noqa
        from collections import deque
        v = set()
        v.add(0)

        q = deque()
        q.append(0)
        while q:
            room = q.popleft()
            for key in rooms[room]:
                if key not in v:
                    v.add(key)
                    q.append(key)
        return len(v) == len(rooms)


if __name__ == '__main__':
    s = Solution()
    y = s.canVisitAllRooms([[1], [2], [3], []])
    print(y)
