class Solution(object):
    def combinationSum2(self, candidates, target):
        """
        求candidates列表中和为target的组合（同一个数只能使用一次)

        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        result = []
        if candidates is []:
            return []
        candidates.sort()

        def combination(start=0, sum_per=0, path=[]):
            # if sum_per == target:
            #     result.append(path)
            #     return
            i = start
            while i < len(candidates):
                sum_current = sum_per + candidates[i]
                if sum_current == target:
                    result.append(path + [candidates[i]])
                if sum_current < target and i + 1 < len(candidates):
                    combination(i + 1, sum_current, path + [candidates[i]])
                while i < len(candidates) - 1 and candidates[i] == candidates[
                            i + 1]:
                    i += 1
                i += 1

        combination()
        return result


if __name__ == '__main__':
    s = Solution()
    print(s.combinationSum2([1, 1], 1))
