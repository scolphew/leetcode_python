class Solution(object):
    def fractionToDecimal(self, numerator, denominator):
        """
        :type numerator: int
        :type denominator: int
        :rtype: str
        """
        if not numerator % denominator:
            return str(numerator // denominator)
        s = {}

        res = "" if numerator * denominator > 0 else "-"
        numerator, denominator = abs(numerator), abs(denominator)
        a, numerator = divmod(numerator, denominator)
        res += str(a) + "."
        index = len(res)
        while numerator:
            if numerator in s:
                start_cycle = s[numerator]
                res = "{}({})".format(res[:start_cycle], res[start_cycle:])
                return res

            s[numerator] = index
            a, numerator = divmod(numerator * 10, denominator)
            res += str(a)
            index += 1
        return res


if __name__ == '__main__':
    s = Solution()
    print(s.fractionToDecimal(10, 99))
    print(s.fractionToDecimal(1110, 9999))
    print(s.fractionToDecimal(1, 3))
    print(s.fractionToDecimal(123, 4))
    print(s.fractionToDecimal(0, 3))
    print(s.fractionToDecimal(1, 4))
    print(s.fractionToDecimal(2, 5))
    print(s.fractionToDecimal(-50, 8))
    print(s.fractionToDecimal(7, -12))
