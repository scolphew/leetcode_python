class Solution:
    def subarrayBitwiseORs(self, arr: list[int]) -> int:
        """
        :param arr: 非空
        """
        ans = set()
        cur = {0}
        for num in arr:
            cur = {num | x for x in cur} | {num}  # cur 最大长度为 log(max num)
            ans |= cur
        return len(ans)


if __name__ == "__main__":
    s = Solution()
    y = s.subarrayBitwiseORs([1, 43, 5, 34, 656, 234, 67, 23, 765, 24, 6, 2, 6, 45, 5])
    print(y)
