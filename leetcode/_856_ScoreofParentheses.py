class Solution:
    def scoreOfParentheses(self, s: str) -> int:  # noqa
        stack = []
        cur = 0
        for c in s:
            if c == '(':
                stack.append(c)
            else:
                while stack[-1] != '(':
                    cur += stack.pop()
                stack[-1] = cur * 2 if cur else 1
                cur = 0

        return sum(stack)


if __name__ == "__main__":
    solution = Solution()
    print(solution.scoreOfParentheses('()'))
    print(solution.scoreOfParentheses('()()()'))
    print(solution.scoreOfParentheses('()(()())'))
    print(solution.scoreOfParentheses('(()(()))'))
