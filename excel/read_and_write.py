import xlrd
import xlsxwriter
import sys


def input_file_name():
    v1 = input("源文件名")
    v2 = input("目标文件名")
    sheet = input("工作表名")
    return v1, v2, sheet


def get_file_name():
    if len(sys.argv) > 1:
        return sys.argv[1], sys.argv[2], sys.argv[3]
    else:
        return input_file_name()


def is_bad_case(key):
    """
    判断是否是bad case
    :param key:
    :return:
    """
    return False


def copy_data():
    v1_name, v2_name, sheet_name = get_file_name()
    data = xlrd.open_workbook(v1_name)
    table = data.sheet_by_name(sheet_name)
    workbook = xlsxwriter.Workbook(v2_name)
    sheet = workbook.add_worksheet(sheet_name)
    index = 0
    for i in range(table.nrows):
        if not is_bad_case(table.cell(i, 0).value):
            for j in range(table.ncols):
                sheet.write(index, j, table.cell(i, j).value)
            index += 1
    workbook.close()


if __name__ == '__main__':
    copy_data()
