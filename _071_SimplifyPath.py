class Solution(object):
    def simplifyPath(self, path):
        """
        简化一个linux绝对  路径

        :type path: str
        :rtype: str
        """
        stack = []
        for each in path.split("/"):
            if each == "..":
                if stack:
                    stack.pop()
            elif each == '.' or each == "":
                pass
            else:
                stack.append(each)
        return '/' + '/'.join(stack)[:]


if __name__ == '__main__':
    s = Solution()
    print(s.simplifyPath("/.."))
