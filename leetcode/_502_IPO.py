class Solution(object):
    def findMaximizedCapital(self, k, W, Profits, Capital):
        """
        :type k: int
        :type W: int
        :type Profits: List[int]
        :type Capital: List[int]
        :rtype: int
        """
        heap = []
        projects = sorted(zip(Profits, Capital), key=lambda l: l[1])
        index = 0

        for i in range(k):
            while index < len(projects):
                if projects[index][1] > W:
                    break
                else:
                    self.heap_add(heap, projects[index][0])
                index += 1
            if not heap:
                break
            else:
                W += self.heap_poll(heap)
        return W

    @staticmethod
    def heap_poll(heap):
        """堆弹出"""
        if len(heap) == 1:
            return heap.pop()
        ans = heap[0]
        heap[0] = heap[-1]
        heap.pop()
        length = len(heap) - 1

        def adjust_heap(i, ):
            l_child = i * 2 + 1
            r_child = l_child + 1
            _max = i
            if i <= (length - 1) // 2:
                if l_child <= length and heap[l_child] > heap[_max]:
                    _max = l_child
                if r_child <= length and heap[r_child] > heap[_max]:
                    _max = r_child
                if _max != i:
                    heap[i], heap[_max] = heap[_max], heap[i]
                    adjust_heap(_max)

        adjust_heap(0)
        return ans

    @staticmethod
    def heap_add(heap, val):
        """堆添加"""
        if not heap:
            heap.append(val)
        else:
            heap.append(val)
            i = len(heap) - 1
            while i > 0:
                parent = (i - 1) >> 1
                if heap[parent] >= val:
                    break
                heap[i] = heap[parent]
                i = parent
            heap[i] = val


if __name__ == '__main__':
    s = Solution()
    print(s.findMaximizedCapital(2, 0, [1, 2, 3], [0, 1, 1]))

    a = []
    for i in range(20):
        s.heap_add(a, i)

    while a:
        print(s.heap_poll(a))
