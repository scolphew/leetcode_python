def p(lst_lst, n=2):
    """
    输出List[list], n表示最大位数
    :param lst_lst:
    :return:
    """
    for i in lst_lst:
        for j in i:
            if type(j) is int:
                print("%02d" % j, end=' ')
            else:
                print(j, end=' ')
        print()
