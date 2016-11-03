class Solution(object):
    def multiply(self, num1, num2):
        """
        string乘法

        :type num1: str
        :type num2: str
        :rtype: str
        """
        len_1 = len(num1)
        len_2 = len(num2)
        result = [0 for _ in range(len_1 + len_2)]
        print(result)
        for i in range(len_1 - 1, -1, -1):
            for j in range(len_2 - 1, -1, -1):
                num = int(num1[i]) * int(num2[j])
                p1 = i + j
                p2 = p1 + 1
                sum_num = num + result[p2]

                result[p1] += sum_num // 10
                result[p2] = sum_num % 10
        r = []
        for i in result:
            if r or i != 0:
                r.append(str(i))
        result = ''.join(r)
        return result if result else '0'

s = Solution()
print(s.multiply("00", "009"))
