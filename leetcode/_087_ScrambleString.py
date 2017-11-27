"""
Given a string s1, we may represent it as a binary tree by partitioning it to two
 non-empty substrings recursively.
* Below is one possible representation of s1 = "great":
*     great
*    /    \
*   gr    eat
*  / \    /  \
* g   r  e   at
*            / \
*           a   t
*
* To scramble the string, we may choose any non-leaf node and swap its two children.
*
* For example, if we choose the node "gr" and swap its two children, it produces a scrambled string "rgeat".
*
*     rgeat
*    /    \
*   rg    eat
*  / \    /  \
* r   g  e   at
*            / \
*           a   t
*
* We say that "rgeat" is a scrambled string of "great".
*
* Similarly, if we continue to swap the children of nodes "eat" and "at", it produces a scrambled string "rgtae".
*
*     rgtae
*    /    \
*   rg    tae
*  / \    /  \
* r   g  ta  e
*        / \
*       t   a
*
* We say that "rgtae" is a scrambled string of "great".
*
* Given two strings s1 and s2 of the same length, determine if s2 is a scrambled string of s1.
"""


class Solution(object):
    def isScramble(self, s1, s2):
        """
        判断两个字符串是否为变体（）
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        len_1 = len(s1)
        len_2 = len(s2)
        if len_1 != len_2 or len_1 == 0 or len_2 == 0:
            return False
        if s1 == s2:
            return True
        letters = [0] * 26
        for i in range(len_1):
            letters[ord(s1[i]) - 97] += 1
            letters[ord(s2[i]) - 97] -= 1
        for i in letters:
            if i != 0:
                return False
        for i in range(1, len_1):
            if self.isScramble(s1[:i], s2[:i]) and self.isScramble(s1[i:],
                                                                   s2[i:]):
                return True
            j = len_1 - i
            if self.isScramble(s1[:i], s2[j:]) and self.isScramble(s1[i:],
                                                                   s2[:j]):
                return True
        return False


if __name__ == '__main__':
    s = Solution()
    print(s.isScramble("eatrg", "great"))
