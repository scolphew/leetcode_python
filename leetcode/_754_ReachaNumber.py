class Solution:
    def reachtarget(self, target):
        target = abs(target)
        sum_ = 0
        i = 1
        while True:
            sum_ += i
            if sum_ == target:
                return i
            elif sum_ > target:
                diff = sum_ - target
                if diff & 1 == 0:
                    return i
                return (i + 2) if (i & 1) else (i + 1)
            i += 1



if __name__ == '__main__':
    s = Solution()
    for i in range(1,1000):
        print(s.reachtarget(i) == s.reachtarget2(i))
