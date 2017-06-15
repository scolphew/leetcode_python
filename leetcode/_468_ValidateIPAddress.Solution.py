class Solution(object):
    def validIPAddress(self, IP):
        """
        :type IP: str
        :rtype: str
        """

        def is_hex(s):
            hex_digits = set("0123456789abcdefABCDEF")
            for char in s:
                if char not in hex_digits:
                    return False
            return True

        ary = IP.split('.')
        if len(ary) == 4:
            for i in ary:
                if not i.isdigit() or not 0 <= int(i) < 256 or (
                                i[0] == '0' and len(i) > 1):
                    return "Neither"
            return "IPv4"
        ary = IP.split(':')
        if len(ary) == 8:
            for i in ary:
                if len(i) == 0 or not len(i) <= 4 or not is_hex(i):
                    return "Neither"
            return "IPv6"
        return "Neither"


if __name__ == '__main__':
    s = Solution()
    print(s.validIPAddress("127.0.0.1"))
    print(s.validIPAddress("2001:0db8:85a3:0:0:8A2E:0370:7334"))
