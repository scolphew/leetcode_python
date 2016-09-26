def p(lst_lst, n, end='-'*8):
    """
    输出List[list], n表示最大位数
    :param lst_lst:
    :return:
    """
    for i in lst_lst:
        for j in i:
            print("%02d" % j, end=' ')
        print()
