from collections import defaultdict
from typing import List


class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:  # noqa
        ans = defaultdict(int)
        for each in cpdomains:
            count, b = each.split()
            count = int(count)
            ans[b] += count
            for i, c in enumerate(b):
                if c == '.':
                    ans[b[i + 1:]] += count
        return [f"{v} {k}" for k, v in ans.items()]


if __name__ == '__main__':
    s = Solution()
    z = s.subdomainVisits(["900 google.mail.com",
                           "50 yahoo.com",
                           "1 intel.mail.com",
                           "5 wiki.org",
                           ])
    print(z)
