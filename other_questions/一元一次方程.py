import re


def solution(in_put):
    a, b, c = [int(x) for x in re.findall("\d+", in_put)]
    return (c - b) / a


if __name__ == '__main__':
    x = solution("10x+1=3")
    print(x)
