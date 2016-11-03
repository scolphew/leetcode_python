def equal_list_list(a, b):
    a = list(map(frozenset, a))
    b = list(map(frozenset, b))
    return a == b
