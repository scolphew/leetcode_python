import collections


class Solution:
    def shortestSubarray(self, nums: list[int], k: int) -> int:  # noqa
        n = len(nums)
        p = [0 for _ in range(n + 1)]
        p[0] = nums[0]
        for i in range(n):
            p[i + 1] = p[i] + nums[i]
        ans = n + 1
        q = collections.deque()
        for i, sum_ in enumerate(p):
            while q and p[q[-1]] >= sum_:
                q.pop()
            while q and sum_ - p[q[0]] >= k:
                ans = min(ans, i - q.popleft())
            q.append(i)
        return ans if ans < n + 1 else -1


if __name__ == "__main__":
    s = Solution()
    y = s.shortestSubarray([1, 2, 3, 4, -5, 6], 11)
    print(y)
