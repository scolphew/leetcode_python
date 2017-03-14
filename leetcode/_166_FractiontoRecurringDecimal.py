class Solution(object):
    def fractionToDecimal(self, numerator, denominator):
        """
        :type numerator: int
        :type denominator: int
        :rtype: str
        """
        if not numerator % denominator:
            return str(numerator // denominator)
        sign = "" if numerator * denominator > 0 else "-"
        l = []
        s = {}
        numerator, denominator = abs(numerator), abs(denominator)
        a, numerator = divmod(numerator, denominator)
        integer = str(a)
        index = 0
        while True:
            a, numerator = divmod(numerator * 10, denominator)

            if (a, numerator) in s:
                start_cycle = s[(a, numerator)]
                break

            l.append(str(a))
            s[(a, numerator)] = index
            index += 1

        a, b = l[:start_cycle], l[start_cycle:]
        a = "".join(a)
        b = "".join(b)
        b = "" if b == "0" else "({})".format(b)

        return "{}{}.{}{}".format(sign, integer, a, "" if b == "0" else b)


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
