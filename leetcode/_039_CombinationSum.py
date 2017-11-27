class Solution(object):
    def combinationSum(self, candidates, target):
        """
        求candidates列表中和为target的组合（同一个数可以多次使用）

        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        result = []
        if candidates is []:
            return []

        def combination(start=0, sum_per=0, path=[]):
            # if sum_per == target:
            #     result.append(path)
            #     return
            for i in range(start, len(candidates)):
                sum_current = sum_per + candidates[i]
                if sum_current == target:
                    result.append(path + [candidates[i]])
                if sum_current < target:
                    combination(i, sum_current, path + [candidates[i]])

        combination()
        return result


if __name__ == '__main__':
    s = Solution()
    print(s.combinationSum([1, 2, 3, 4, 5], 7))
