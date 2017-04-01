def search(nums, target, left=None, right=None) -> int:
    """
    寻找target的下标，不存在则返回-1
    @:param:nums 不带重复元素的数组
    """
    if left is None:
        left = 0
    if right is None:
        right = len(nums) - 1
    while left <= right:
        mid = (left + right) >> 1
        if nums[mid] == target:
            return mid
        if nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1


def search_lt(nums, target, left=None, right=None):
    """
    寻找比target小的最大下标，不存在则返回-1
    """
    if left is None:
        left = 0
    if right is None:
        right = len(nums) - 1
    while left < right - 1:
        mid = (left + right) >> 1
        if nums[mid] < target:
            left = mid
        else:
            right = mid - 1
    if nums[right] < target:
        return right
    if nums[left] < target:
        return left
    return -1


def search_gt(nums, target, left=None, right=None):
    """
    寻找比target大的最小下标，不存在则返回-1
    """
    if left is None:
        left = 0
    if right is None:
        right = len(nums) - 1
    while left < right:
        mid = (left + right) >> 1
        if nums[mid] <= target:
            left = mid + 1
        else:
            right = mid
    if nums[right] > target:
        return right
    return -1


def search_first(nums, target, left=None, right=None):
    """
    寻找target的下标，不存在则返回-1
    @:param:nums 不带重复元素的数组
    """
    if left is None:
        left = 0
    if right is None:
        right = len(nums) - 1
    while left < right:
        mid = (left + right) >> 1
        if nums[mid] < target:
            left = mid + 1
        else:
            right = mid
    if nums[left] == target:
        return left
    return -1


def search_last(nums, target, left=None, right=None):
    """
    寻找target最后一次出现的下标，不存在则返回-1
    @:param:nums 可以带重复元素的数组
    """
    if left is None:
        left = 0
    if right is None:
        right = len(nums) - 1
    while left < right - 1:
        mid = (left + right) >> 1
        if nums[mid] <= target:
            left = mid
        else:
            right = mid
    if nums[right] == target:
        return right
    if nums[left] == target:
        return left
    return -1


def lower_bound(nums, key, first=0, length=None):
    """
    返回nums中大于等于key的最小下标，
    或者说，
    向nums中插入key时，应该插入到什么位置"""
    if length is None:
        length = len(nums)
    while length > 0:
        half = length >> 1
        mid = first + half
        if nums[mid] < key:
            first = mid + 1
            length -= half + 1
        else:
            length = half
    return first


def upper_bound(nums, key, first=0, length=None):
    """
    返回nums中第一个大于key的位置
    """
    if length is None:
        length = len(nums)
    while length > 0:
        half = length >> 1
        mid = first + half
        if nums[mid] > key:
            length = half
        else:
            first = mid + 1
            length -= half + 1
    return first


if __name__ == '__main__':
    print(search_lt([1, 2, 2, 2, 2, 2, 2, 2, 3], 2))
