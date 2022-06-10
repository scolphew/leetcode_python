import bisect
from typing import List


class Solution:
    def maxProfitAssignment(self, difficulty: List[int], profit: List[int], worker: List[int]) -> int:  # noqa
        jobs = [[d, profit[i]] for i, d in enumerate(difficulty)]
        jobs.sort()
        max_profile = 0
        for job in jobs:
            max_profile = max(max_profile, job[1])
            job[1] = max_profile

        ans = 0
        for each in worker:
            i = bisect.bisect_right(jobs, [each, 100001])
            if i > 0:
                ans += jobs[i - 1][1]
        return ans


if __name__ == '__main__':
    s = Solution()
    x = s.maxProfitAssignment([68, 35, 52, 47, 86],
                              [67, 17, 1, 81, 3],
                              [92, 10, 85, 84, 82]
                              )
    print(x)
