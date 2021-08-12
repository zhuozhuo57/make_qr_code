# 测试一个截取关键字的片段
# 读取LOG日志，截取detect recognition 1:n 比较时间平均值

import openpyxl


def str_dict(path):
    # test_result_path={"":""}

    # test_result_path=open(test_result_path,"r").read(100)
    # test_result_path=open(test_result_path,"r").readline(1000)
    # 上面是str
    # test_result_path=open(test_result_path,"r").readlines(-10)
    # list
    test_result_path = openpyxl.load_workbook(path)
    print(type(test_result_path))
    print(test_result_path)

    dict = dict(test_result_path)
    print(dict)
    print(type(dict))


if __name__ == "__main__":
    str_dict('20210727barcoderesult.txt')
