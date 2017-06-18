class Solution(object):
    def findAllConcatenatedWordsInADict(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        ans = []
        words = set(words)

        def search(w):
            if w in words:
                return True
            for i in range(1, len(w)):
                if w[:i] in words and search(w[i:]):
                    return True
            return False

        for word in words:
            words.remove(word)
            if search(word):
                ans.append(word)
            words.add(word)
        return ans


if __name__ == '__main__':
    s = Solution()
    print(s.findAllConcatenatedWordsInADict(
        ["cat", "cats", "catsdogcats", "dog", "dogcatsdog", "hippopotamuses",
         "rat", "ratcatdogcat"]))
