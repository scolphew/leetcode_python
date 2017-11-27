class Solution(object):
    def restoreIpAddresses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        result = []
        len_ip = len(s)

        def dfs(start=0, step=0, ip=""):
            if start == len_ip and step == 4:
                result.append(ip[:-1])
                return
            if len_ip - start > 3 * (4 - step):
                return
            if len_ip - start < 4 - step:
                return
            num = 0
            for i in range(start, min(start + 3, len_ip)):
                num = num * 10 + int(s[i])
                if num <= 255:
                    ip += s[i]
                    dfs(i + 1, step + 1, ip + '.')
                if num == 0:
                    break;

        dfs()
        return result


if __name__ == "__main__":
    s = Solution()
    x = s.restoreIpAddresses("25525511135")
    print(x)
