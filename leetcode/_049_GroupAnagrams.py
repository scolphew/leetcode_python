class Solution(object):
    def groupAnagrams(self, strs: list) -> list:
        """
        str的数组，对相同字母组成的为一类，分类

        :type strs: List[str]
        :rtype: List[List[str]]
        """
        result = []
        words = {}
        for string in strs:
            s = tuple(sorted(list(string)))
            if s in words:
                result[words[s]].append(string)
            else:
                words[s] = len(result)
                result.append([string])
        return result

    def group2(self, strs):
        from collections import defaultdict
        retdict = defaultdict(list)
        for i in strs:
            nums = [0] * 26
            for j in i:
                nums[ord(j) - 97] += 1
            retdict[tuple(nums)].append(i)
        return list(retdict.values())

if __name__ == '__main__':
    s = Solution()
    print(s.groupAnagrams(["aab", "abb", "tan", "ate", "nat", "bat"]))
    print(s.groupAnagrams([""]))
    print(s.groupAnagrams([]))