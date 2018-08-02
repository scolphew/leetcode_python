class Solution(object):
    def findDuplicate(self, paths):
        """
        :type paths: List[str]
            每个path的格式"{目录} {文件名1(文件内容1)}{文件名n(文件内容n)}"
        :rtype: List[List[str]]
            内容重复问所有文件的路径的所有路径
        """
        from collections import defaultdict
        d = defaultdict(list)
        for path in paths:
            # path = "root/a 1.txt(abcd) 2.txt(efgh)"
            lst = path.split()
            p = lst[0]
            for each in lst[1:]:
                i = each.index('(')
                file_name = each[:i]
                file_content = each[i + 1:-1]
                d[file_content].append("{}/{}".format(p, file_name))
        return [i for i in d.values() if len(i) > 1]


if __name__ == '__main__':
    s = Solution()
    print(s.findDuplicate(["root/a 1.txt(abcd) 2.txt(efgh)",
                           "root/c 3.txt(abcd)",
                           "root/c/d 4.txt(efgh)",
                           "root 4.txt(efgh)"]))
