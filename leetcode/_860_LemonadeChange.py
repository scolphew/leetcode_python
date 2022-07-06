from typing import List


class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:  # noqa
        a, b = 0, 0
        for bill in bills:
            if bill == 5:
                a += 1
            elif bill == 10:
                if a:
                    a -= 1
                    b += 1
                else:
                    return False
            else:
                if b > 0 and a > 0:
                    a -= 1
                    b -= 1
                elif a >= 3:
                    a -= 3
                else:
                    return False
        return True


if __name__ == "__main__":
    s = Solution()
    y = s.lemonadeChange([5, 5, 10, 20, 5, 5, 5, 5, 5, 5, 5, 5, 5, 10, 5, 5, 20, 5, 20, 5])
    print(y)
