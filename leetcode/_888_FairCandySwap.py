class Solution:
    def fairCandySwap(self, aliceSizes: list[int], bobSizes: list[int]) -> list[int]:  # noqa
        sum_a, sum_b = sum(aliceSizes), sum(bobSizes)
        delta = (sum_a - sum_b) // 2
        rec = set(aliceSizes)
        ans = None
        for y in bobSizes:
            x = y + delta
            if x in rec:
                ans = [x, y]
                break
        return ans
