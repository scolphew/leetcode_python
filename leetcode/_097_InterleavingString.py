class Solution(object):
    def isInterleave(self, s1, s2, s3):
        """
        判断s3是否由s2交叉之后的结果
        :type s1: str
        :type s2: str
        :type s3: str
        :rtype: bool
        """
        len1 = len(s1)
        len2 = len(s2)
        len3 = len(s3)
        if len1 + len2 != len3:
            return False
        flag = [[False] * (len1 + 1) for i in range(len2 + 1)]
        flag[0][0] = True
        for i in range(len1):
            if s1[i] == s3[i]:
                flag[0][i + 1] = True
            else:
                break
        for i in range(len2):
            if s2[i] == s3[i]:
                flag[i + 1][0] = True
            else:
                break
        for j in range(len1):
            for i in range(len2):
                flag[i + 1][j + 1] = True if flag[i][j + 1] and s3[
                                                                    i + j + 1] == \
                                                                s2[
                                                                    i] else True if \
                flag[i + 1][j] and s3[i + j + 1] == s1[j] else False
        for i in range(len2 + 1):
            print(flag[i])


if __name__ == "__main__":
    s = Solution()
    x = s.isInterleave("aabcc", "dbbca", "aadbbcbcac")
    print(x)
    x = s.isInterleave("aabcc", "dbbca", "aadbbbaccc")
    print(x)
