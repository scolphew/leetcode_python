class Solution(object):
    def findSubstring(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: List[int]
        """
        indices = []

        if len(s) == 0 or len(words) == 0:
            return indices
        # 单词长度
        word_len = len(words[0])
        # 要匹配的长度
        length = len(words) * word_len
        if len(s) < length:
            return indices

        word_dist = {}
        for word in words:
            word_dist[word] = word_dist.get(word, 1)

        index = 0
        while index < word_len:
            start =index_1 = index
            hash_word = {}
            counter = 0
            while index_1 < len(s):
                # 取一个词
                comparator = s[index_1:index_1 + word_len]
                if comparator not in word_dist:
                    index_1 += word_len
                    counter = 0
                    start = index_1
                    hash_word = {}
                    continue

                if comparator in hash_word and hash_word[comparator] == \
                        word_dist[comparator]:
                    hash_word[s[start:start + word_len]] -= 1
                    start += word_len
                    counter -= 1
                    continue

                hash_word[comparator] = hash_word.get(comparator, 1)
                counter += 1

                if counter == len(words):
                    indices.append(start)
                    hash_word[s[start:start + word_len]] -= 1
                    start += word_len
                    counter -= 1
                    index_1 += word_len
                    continue

                index_1 += word_len

            index += 1

        return indices


if __name__ == '__main__':
    s = Solution()
    print(s.findSubstring("barfoothefoobarman", ["foo", "bar"]))
