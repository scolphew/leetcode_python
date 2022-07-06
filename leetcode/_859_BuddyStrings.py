from collections import Counter


class Solution:
    def buddyStrings(self, s: str, goal: str) -> bool:  # noqa
        if len(s) != len(goal):
            return False
        if s == goal:
            c = Counter(s)
            return any(n > 1 for _, n in c.items())
        else:
            z = [(a, b) for a, b in zip(goal, s) if a != b]
            return len(z) == 2 and z[0] == z[1][::-1]


if __name__ == '__main__':
    s = Solution()
    print(s.buddyStrings("abc", "acb"))
