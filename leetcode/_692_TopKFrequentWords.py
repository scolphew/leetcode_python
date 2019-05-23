from typing import List


class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        from heapq import heappush, heappop
        d = {}
        for word in words:
            d[word] = d.get(word, 0) + 1
        l = []
        for key, value in d.items():
            heappush(l, (-value, key))
        return [heappop(l)[1] for _ in range(k)]


if __name__ == '__main__':
    s = Solution()
    print(s.topKFrequent(
        ["the", "day", "is", "sunny", "the", "the", "the", "sunny", "is", "is"]
        , 4))
