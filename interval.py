class Interval(object):
    """表示start到stop的数字区间"""

    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

    def __repr__(self):
        return str(self.start) + "-" + str(self.end)
