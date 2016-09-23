class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        result = []
        if candidates is []:
            return []

        def combination(start=0, sum_num=0, path=[]):
            if sum_num == target:
                result.append(path)
                return
            for i in range(start, len(candidates)):
                s = sum_num + candidates[i]
                if s <= target:
                    combination(i, s, path + [candidates[i]])

        combination()
        return result

s = Solution()
print(s.combinationSum([1, 2, 3, 4, 5], 7))
