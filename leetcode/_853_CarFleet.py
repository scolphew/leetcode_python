from typing import List


class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:  # noqa
        cats = zip(position, speed)
        cats = sorted(cats)
        pre_time = 0
        ans = 0
        for cat_p, car_s in cats[::-1]:
            target_time = (target - cat_p) / car_s
            if target_time > pre_time:  # 追不上
                pre_time = target_time
                ans += 1
        return ans


if __name__ == "__main__":
    s = Solution()
    y = s.carFleet(12, [10, 8, 0, 5, 3], [2, 4, 1, 1, 3])
    print(y)
