from typing import List


class Solution:
    def partitionLabels(self, S: str) -> List[int]:
        d = {c: i for i, c in enumerate(S)}
        ans = []
        start = max_ = 0
        for i, c in enumerate(S[1:]):
            max_ = max(max_, d[c])
            if max_ == i:
                ans.append(i - start + 1)
                start = i + 1
        return ans


if __name__ == '__main__':
    s = Solution()
    print(s.partitionLabels("ababcbacadefegdehijhklij"))
