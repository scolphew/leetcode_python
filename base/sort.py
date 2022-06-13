def quick_sort(nums):
    """快速排序"""

    def q_sort(l, r):
        left, right = l, r
        if l >= r:
            return
        tmp = nums[l]
        while l < r:
            while l < r and nums[r] >= tmp:
                r -= 1
            nums[l] = nums[r]
            while l < r and nums[l] <= tmp:
                l += 1
            nums[r] = nums[l]
        nums[l] = tmp
        q_sort(left, l - 1)
        q_sort(l + 1, right)

    q_sort(0, len(nums) - 1)


def quick_sort2(nums):
    def q_sort(l, r):
        if l >= r:
            return
        tmp = nums[l]
        i = l
        for j in range(l + 1, r + 1):
            if a[j] <= tmp:
                i += 1
                a[i], a[j] = a[j], a[i]
        else:
            a[l], a[i] = a[i], a[l]

        q_sort(l, i - 1)
        q_sort(i + 1, r)

    q_sort(0, len(nums) - 1)


def merge_sort(nums):
    """归并排序"""

    def merge(nums, left, mid, right):
        tmp = []
        i = left
        j = mid + 1
        while i <= mid and j <= right:
            if nums[i] < nums[j]:
                tmp.append(nums[i])
                i += 1
            else:
                tmp.append(nums[j])
                j += 1
        tmp.extend(nums[i:mid + 1])
        tmp.extend(nums[j:right + 1])
        nums[left:right + 1] = tmp

    def m_sort(nums, l, r):
        if l < r:
            mid = (l + r) >> 1
            m_sort(nums, l, mid)
            m_sort(nums, mid + 1, r)
            merge(nums, l, mid, r)

    m_sort(nums, 0, len(nums) - 1)


def heap_sort(nums):
    """堆排序"""
    length = len(nums) - 1

    def adjust_heap(i):

        l_child = i * 2 + 1
        r_child = l_child + 1
        _max = i
        if i <= (length - 1) // 2:
            if l_child <= length and nums[l_child] > nums[_max]:
                _max = l_child
            if r_child <= length and nums[r_child] > nums[_max]:
                _max = r_child
            if _max != i:
                nums[i], nums[_max] = nums[_max], nums[i]
                adjust_heap(_max)

    def init_heap():
        for i in range((length - 1) // 2, -1, -1):
            adjust_heap(i)

    init_heap()
    while length > 0:
        nums[0], nums[length] = nums[length], nums[0]
        length -= 1
        adjust_heap(0)
    print(nums)


def insert_sort(nums):
    """直接插入排序"""
    length = len(nums)
    i = 1
    while i < length:
        # for j in range(i, 0, -1):
        #     if nums[j] < nums[j - 1]:
        #         nums[j], nums[j - 1] = nums[j - 1], nums[j]
        #     else:
        #         break
        tmp = nums[i]
        j = i - 1
        while j >= 0 and tmp < nums[j]:
            nums[j + 1] = nums[j]
            j -= 1
        a[j + 1] = tmp
        i += 1


def shell_sort(nums):
    """希尔排序"""
    length = len(nums)

    def shell_insert_sort(d):
        for i in range(d, length):
            tmp = nums[i]
            j = i - d
            while j >= 0 and tmp < nums[j]:
                a[j + d] = a[j]
                j = j - d
            a[j + d] = tmp

    d = length // 2
    while d > 0:
        shell_insert_sort(d)
        print(d, nums)
        d //= 2


def select_sort(nums):
    length = len(nums)

    def select_min(i):
        min_key = i
        for key, value in enumerate(nums[i + 1:], i + 1):
            if value < nums[min_key]:
                min_key = key
        return min_key

    for i in range(length):
        key = select_min(i)
        if i != key:
            nums[i], nums[key] = nums[key], nums[i]


if __name__ == '__main__':
    a = [2, 7, 8, 3, 1, 6, 9, 0, 5, 4]
    print(a)
    quick_sort2(a)
    print(a)
