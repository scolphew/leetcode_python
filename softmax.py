"""
把邮箱转换成softmax值，再转回来
"""
import numpy as np

def softmax(x):
    """Compute softmax values for each sets of scores in x."""
    e_x = np.exp(x)
    return e_x / e_x.sum()


def softmax2(x):
    import math
    sum = 0
    for i in x:
        i -= max(x)
    i = 0
    while i < len(x):
        sum = sum / (i + 1) * i + math.exp(x[i]) / (i + 1)
        i += 1
    return [math.exp(i) / sum / len(x) for i in x]

def inverse_softmax(z):
    xx = math.exp(ord('@') - ord('.'))
    l = len(z)
    m, n = 0, 0
    for i in range(1, l):
        for j in range(i + 1, l):
            if z[i] // z[j] == xx // 1:
                m, n = i, j
                bz = math.log(z[m] / math.exp(ord('@'))) // 1
                xxx = []
                for k in z:
                    diff = math.log(z[m] / k) // 1
                    xxx.append(chr(int(ord('@') - diff)))
                print(''.join(xxx))

import math

a = "scolphew@qq.com"
scores = [ord(i) for i in a]
z = softmax2(scores)
inverse_softmax(z)

