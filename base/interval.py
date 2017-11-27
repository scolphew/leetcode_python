class Interval(object):
    """表示start到stop的数字区间"""

    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

    def __repr__(self):
        return str(self.start) + "-" + str(self.end)


def get_intervals(pairs):
    b = []
    for x in pairs:
        assert len(x) == 2
        b.append(Interval(x[0], x[1]))
    return b
