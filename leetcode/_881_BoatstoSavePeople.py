class Solution:
    def numRescueBoats(self, people: list[int], limit: int) -> int:  # noqa
        ans = 0
        people.sort()
        left, right = 0, len(people) - 1
        while left <= right:
            if people[left] + people[right] > limit:
                right -= 1
            else:
                right -= 1
                left += 1
            ans += 1
        return ans


if __name__ == "__main__":
    s = Solution()
    y = s.numRescueBoats([1, 2, 3, 2], 3)
    print(y)
