import configparser
import os
import re

import openpyxl

file = os.path.dirname(os.path.abspath(__file__))
config = configparser.ConfigParser()
print(config)
s = config.read(file + r'\config.ini')
excelPath = config.get("Local", "ResultPath")
filePath = config.get("Local", "logPath")
tempfile = config.get("Local", "temp")
data = openpyxl.load_workbook(excelPath)
sheet = data['Sheet1']
sheet.cell(1, 1).value = 'date_time'
sheet.cell(1, 2).value = "version"
sheet.cell(1, 3).value = "dataset_path"

# sheet.cell(1, 4).value = "code_type"
with open(filePath, 'r', encoding="utf-8") as f:
    readlines = f.readlines()
    print("readlines  is ", readlines)
    i = 0
    for s in readlines:
        i += 1
        print("i number is", i)
        if ('date_time' in s):
            # print("date_time is",s)
            # date_time = re.findall(r'"date_time":(.*)"version":(.*),"dataset_path":(.*)',s)
            date_time = re.findall(r'"date_time":(.*),"version":(.*),"dataset_path":(.*)', s)
            # print("date_time is" ,date_time)
            # print("date_time type  is" ,type(date_time))
            # date_time[0]
            # 实现提取date_time
            # print(date_time[0])
            # print(type(date_time[0]))
            # 实现date_time_value 写入
            date_time_value = date_time[0][0]
            # print("date_time_value is",date_time_value)
            # print(type((date_time[0])[0]))
            sheet.cell(2, 1).value = date_time_value
            data.save(excelPath)
            # 实现version写入
            version = date_time[0][1]
            # print("version_value is",version)
            # print(type((date_time[0])[1]))
            sheet.cell(2, 2).value = version
            data.save(excelPath)
            # 实现dataset_path写入
            dataset_path = date_time[0][2]
            # ("dataset_path is",dataset_path)
            # print(type((date_time[0])[2]))
            sheet.cell(2, 3).value = dataset_path
            data.save(excelPath)
        # 实现decode_results 写入
        if ('decode_results' in s):
            sheet.cell(3, 1).value = 'decode_results'
            data.save(excelPath)

        if ('image_path' in s):
            sheet.cell(4, 1).value = 'image_path'
            data.save(excelPath)
        if ('succeed' in s):
            sheet.cell(4, 2).value = 'succeed'
            data.save(excelPath)
        if ('run_time' in s):
            sheet.cell(4, 3).value = 'run_time'
            data.save(excelPath)
        if ('results' in s):
            sheet.cell(4, 4).value = 'results'
            data.save(excelPath)
        if ('image_path' in s):
            # 实现image_name写入表中
            image_path_line = re.findall(r'"image_path":(.*),"succeed":(.*),"run_time":(.*),"results":(.*)', s)
            # print("image_path_line is", image_path_line)
            # print("succeed is", s[1])
            # print("image_path_line type  is", type(image_path_line))
            image_name = image_path_line[0]
            print("s is", s)
            print("image_name is", image_name)
            print("image_name type is", type(image_name))
            sheet.cell(i + 2, 1).value = image_name[0]
            data.save(excelPath)
            # 实现succed写入表中
            succeed = (image_name)[1]
            print("succeed is", succeed)
            print(type(succeed))
            sheet.cell(i + 2, 2).value = succeed
            data.save(excelPath)
            # 实现runtime写入表中
            run_time = (image_name)[2]
            print("run_time is", run_time)
            print(type(run_time))
            sheet.cell(i + 2, 3).value = run_time
            data.save(excelPath)
            # 实现results写入表中
            results = (image_name)[3]
            print("results is", results)
            print(type(results))

            sheet.cell(i + 2, 4).value = results
            data.save(excelPath)
