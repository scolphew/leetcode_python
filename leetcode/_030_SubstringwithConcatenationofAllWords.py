class Solution(object):
    def findSubstring(self, s, words):
        """
        求str中words组合的字符串出现的次数，返回每次出现的索引

        :type s: str
        :type words: List[str] 单词可以重复
        :rtype: List[int]
        """
        result = []

        if len(s) == 0 or len(words) == 0:
            return result
        # 单词长度
        word_len = len(words[0])
        # 要匹配的长度
        length = len(words) * word_len
        if len(s) < length:
            return result

        word_dist = {}
        for word in words:
            word_dist[word] = word_dist.get(word, 0) + 1

        for index in range(word_len):
            index_1 = index
            start = index  # 记录当前循环中的起点
            current_words = {}  # 记录当前循环中的单词
            word_count = 0  # 记录当前循环的单词数量
            while index_1 < len(s):
                this_word = s[index_1:index_1 + word_len]
                # 当前单词不成立,清空重新开始
                if this_word not in word_dist:
                    index_1 += word_len
                    start = index_1
                    current_words = {}
                    word_count = 0
                    continue

                # 当前单词已经多余
                if this_word in current_words and current_words[this_word] == \
                        word_dist[this_word]:
                    # 逐步清除单词，直到这一个
                    while start < len(s):
                        first_word = s[start:start + word_len]
                        current_words[first_word] -= 1
                        word_count -= 1
                        start += word_len
                        if first_word == this_word:
                            break
                    continue

                current_words[this_word] = current_words.get(this_word, 0) + 1
                word_count += 1

                # 如果满足条件
                if word_count == len(words):
                    result.append(start)
                    current_words[s[start:start + word_len]] -= 1  # 去掉第一个
                    word_count -= 1  # 减一个计数
                    start += word_len
                    index_1 += word_len
                    continue

                index_1 += word_len

        return result


if __name__ == '__main__':
    s = Solution()
    print(s.findSubstring(
        "wordgoodgoodgoodbestword"
        ,
        ["word", "good", "best", "good"]
    ))

    print(s.findSubstring(
        "barfoothefoobarman"
        ,
        ["foo", "bar"]
    ))

    print(s.findSubstring(
        "lingmindraboofooowingdingbarrwingmonkeypoundcake"
        ,
        ["fooo", "barr", "wing", "ding", "wing"]
    ))
