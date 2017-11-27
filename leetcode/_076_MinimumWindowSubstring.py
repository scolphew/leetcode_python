class Solution(object):
    def minWindow(self, s, t):
        """
        最短匹配字串（无序）
        :type s: str
        :type t: str
        :rtype: str
        """
        from collections import Counter
        length = len(t)
        i = l = 0
        r = len(s) - 1
        chars = Counter(t)
        for j, c in enumerate(s, 1):
            length -= chars[c] > 0
            chars[c] -= 1
            if not length:
                while i < j and chars[s[i]] < 0:
                    chars[s[i]] += 1
                    i += 1
                if j - i < r - l:
                    l, r = i, j
        return s[l:r]


if __name__ == '__main__':
    s = Solution()
    print(s.minWindow(
        "cabwefgewcwaefgcf",
        "cae"
    ))
