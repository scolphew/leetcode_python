class Solution(object):
    def fullJustify(self, words, maxWidth):
        """
        左右对其
        :type words: List[str]
        :type maxWidth: int
        :rtype: List[str]
        """
        result = []
        length = 0
        num = 0  # 该行记录单词个数
        line = []

        def toStr(words):
            print(words)
            s = ""
            blank = maxWidth - length
            if num == 1:
                return words[0] + ' ' * (maxWidth - len(words[0]))
            blank_num = num - 1
            p = blank // blank_num
            q = blank % blank_num
            for i in range(q):
                s += words[i] + ' ' * (p + 1)
            for i in range(q, blank_num):
                s += words[i] + ' ' * p
            s += words[-1]
            return s

        def lastToStr(words):
            return ' '.join(words) + ' ' * (maxWidth - length - num + 1)

        for word in words:
            if length + len(word) + num > maxWidth:
                result.append(toStr(line))
                line = [word]
                length = len(word)
                num = 1
            else:
                line.append(word)
                length += len(word)
                num += 1
        result.append(lastToStr(line))
        return result


s = Solution()
a = ["My", "momma", "always", "said,", "\"Life", "was", "like", "a", "box",
     "of", "chocolates.", "You", "never", "know", "what", "you're", "gonna",
     "get."]
for i in s.fullJustify(a, 20):
    print(i)
