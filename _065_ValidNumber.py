class Solution(object):
    def isNumber(self, s):
        """
        string is int
        :type s: str
        :rtype: bool
        """
        import re
        digit2 = re.compile(
            "^[ ]*[+-]?(\d+\.?\d*|\d*\.?\d+)(e[+-]?\d+)?[ ]*$")
        return bool(digit2.match(s))

    def isNumber2(self, s):
        """
        :type s: str
        :rtype: bool
        """
        # define a DFA
        state = [{},
                 {'blank': 1, 'sign': 2, 'digit': 3, '.': 4},
                 {'digit': 3, '.': 4},
                 {'digit': 3, '.': 5, 'e': 6, 'blank': 9},
                 {'digit': 5},
                 {'digit': 5, 'e': 6, 'blank': 9},
                 {'sign': 7, 'digit': 8},
                 {'digit': 8},
                 {'digit': 8, 'blank': 9},
                 {'blank': 9}]
        currentState = 1
        for c in s:
            if c >= '0' and c <= '9':
                c = 'digit'
            if c == ' ':
                c = 'blank'
            if c in ['+', '-']:
                c = 'sign'
            if c not in state[currentState].keys():
                return False
            currentState = state[currentState][c]
        if currentState not in [3, 5, 8, 9]:
            return False
        return True


s = Solution()
print(s.isNumber2("3"), True)
print(s.isNumber2("e"), False)
print(s.isNumber2("+e123"), False)
print(s.isNumber2("1e123"), True)
print(s.isNumber2("1.2"), True)
print(s.isNumber2(".2"), True)
print(s.isNumber2("++.2"), False)
print(s.isNumber2("."), False)
