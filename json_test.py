# 实现读取文件内容转换成字典
import json
import sys

sys.setrecursionlimit(1000000)


# def get_txt_line():
#     file = os.path.dirname(os.path.abspath(__file__))
#     config = configparser.ConfigParser()
#     print(config)
#     s = config.read(file + r'\config.ini')
#     excelPath = config.get("Local", "ResultPath")
#     filePath = config.get("Local", "logPath")
#     # tempfile = config.get("Local", "temp")
#     data = openpyxl.load_workbook(excelPath)
#     sheet = data['Sheet1']
#     sheet.cell(1, 1).value = 'date_time'
#     sheet.cell(1, 2).value = "version"
#     sheet.cell(1, 3).value = "dataset_path"


def test():
    # import json

    file = open('QR_DM_V0.10.3.txt', 'r', encoding='utf-8')
    js = file.read()
    dic = json.loads(js)
    print(dic)
    print(type(dic))

    file.close()


# class HandleJson:
#     '''
#     定义一个json格式数据处理类
#     '''
#
#     @staticmethod
#     def loads_data(data):
#         '''
#         将json数据格式的数据转换为字典型的数据类型
#         :param data: json格式字符串
#         :return: 字典数据类型
#         '''
#         dict_ison = json.loads(data)
#         print(dict_ison)
#         return dict_ison
#
#     @staticmethod
#     def load_data(filename):
#         '''
#         读取json文件中的json数据并转换为字典型的数据类型
#         :param filename:json文件名
#         :return:字典数据类型
#         '''
#         with open(filename, mode='r', encoding='utf-8') as fp:
#             dict_file = json.load(fp)
#             print(dict_file)
#         return dict_file
#
#     @staticmethod
#     def dumps_data(data):
#         '''
#         将字典数据类型转换为json格式类型数据
#         :param data: 字典数据类型
#         :return: json格式字符串
#         '''
#         json_dict = json.dumps(data, ensure_ascii=False)
#         return json_dict
#
#     @staticmethod
#     def dump(data, filename):
#         '''
#         将字典数据类型转换为json格式数据并存储到json格式的文件中
#         :param data: 字典数据类型
#         :param filename: json文件名
#         :return: json格式文件
#         '''
#         with open(filename, mode='w', encoding='utf-8') as fp:
#             json.dump(data, fp)

#
# def loads_data(filePath):
#     loads_data(filePath)
#     print()
#     pass


if __name__ == '__main__':
    # get_txt_line()
    test()
    # loads_data('QR_DM_V0.10.3.txt')
