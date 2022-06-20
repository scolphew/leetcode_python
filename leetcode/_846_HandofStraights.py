from typing import List
from collections import Counter


class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:  # noqa
        n = len(hand)
        if n % groupSize != 0:
            return False
        hand.sort()
        cnt = Counter(hand)
        for e in hand:
            if cnt[e] == 0:
                continue
            for num in range(e, e + groupSize):
                if cnt[num] == 0:
                    return False
                cnt[num] -= 1
        return True


if __name__ == "__main__":
    s = Solution()
    y = s.isNStraightHand([1, 2, 3, 6, 2, 3, 4, 7, 8], groupSize=3)
    print(y)
