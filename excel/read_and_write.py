import xlrd
import xlsxwriter

v1_name = "aa.xlsx"  # 源文件名
v2_name = 'bb.xlsx'  # 写入的文件名
sheet_name = "abc"  # 源文件的sheet名字
data = xlrd.open_workbook(v1_name)
table = data.sheet_by_name(sheet_name)


def is_bad_case(key):
    """
    判断是否是bad case
    :param key:
    :return:
    """
    return False


def copy_data():
    workbook = xlsxwriter.Workbook('bb.xlsx')
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
