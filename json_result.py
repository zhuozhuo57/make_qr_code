import configparser
import os
import re

file = os.path.dirname(os.path.abspath(__file__))
config = configparser.ConfigParser()
print(config)
s = config.read(file + r'\config.ini')
excelPath = config.get("Local", "ResultPath")
filePath = config.get("Local", "logPath")
tempfile = config.get("Local", "temp")
with open(filePath, 'r', encoding="utf-8") as f:
    lists = f.read()
    print('list is ', lists)
    new_line = re.findall('{').
    # for line in lists:
    #
    #    # print(line.rstrip(' '))
    #     a=line.rstrip('[').rstrip(']').rstrip('{').rstrip("}")
    #     print("a is",a)
    # print(type(a))
    # print(a.rsplit(' '))
    # b=a.rsplit(' ')
    # print("b is ",b)
    # print(a.rsplit(' '))
    # .split(','))
    # print(a.replace('            [\n,',' ',200000))
    # print(a.replace('    }',' ',200000))
    # b=a.replace('\n',' ',200000).rstrip('\n')
    # print('ssdfsdfsd',a.replace('\n',' ',200000).rstrip('\n').rstrip(']').rstrip('[').rstrip('{').rstrip('}'))
    # dict=b.split(',')
    # print("dict is",dict)
    # print(dict.remove(''))
    # b=line.split(',')
    # print(b)
    # print(type(a))

    # b=a.split('\n')
    # print(a.split(','))
    # print(b.s)
    # print(type(a))
    # print(type(line.rstrip(' ')))
    # print(type(line.split(',')))
    # print(list.remove('{\n'))
    # print(list.remove(''))
    # print(list)
    # print(list.index('1'))
    # print(list.append('333'))
    # print(list)
    # print(list.index('333'))
    # print(list.remove('2'))
    # print(list)
    # print(list.append('7777'))
    # print(list.append('12'))
    # print(list.sort())
    # print(list)
    # print(list.clear())
    # print(list.append('7777'))
    # print(list)
    # print(list.append('7777'))
    # print(list.copy().count('7777'))
    # print(list)
    # print(list.extend(list[0]))
    # print(list.extend(list[3]))
    # print(list)
    # print(list.extend('ee'))
    #
    # print(list)
    # print(list.remove('2'))
    #
    # print(list.pop())#删除最后一位
    # print(list)
    # print(list.pop(-4))
    # print(list)
    # # print(list.__add__(list))
    # print(list.reverse())
    #
    # print(list)
    # print(list.sort())
    # print(list.append("\n"))
    # print(list)
    # print(list.__delattr__())
    # #print(list.__format__("\n"))
    # print(list)

    # if i < len(a):
    #
    #     print(str(a[i].split(',')).strip('\n'))
    #     i+=1
    # # for readline in readlines:
    # #     strss=readline.split('\n')
    # #     print(strss)
    # #     str_0=str(strss[0])
    # #     print("str_0is",str_0)
    # files = open(tempfile, 'w', encoding='utf-8')
    # for line in readlines:
    #     # if ('result : ' in line):
    #     #     line = line.replace('result : ', ':null \n')
    #     #     print("line is ", line)
    #     #     print(type(line))
    #     #     file.write(line)
    #     image_line = re.findall(r':(.*).png', line)
    #     print("image_line is", image_line)
    #     print("line is", line)
    #     print(type(image_line))
    #     if (image_line == '[]'):
    #         continue
    #     files.write(str(image_line))
    #     duration = re.findall(r'duration :(.*)ms', line)
    #     if (duration != '[]'):
    #         continue
    #         files.write(str(duration))
    #     # files.close()
    #     result = re.findall(r'result :(.*)', line)
    #     if (result != '[]'):
    #         continue
    #         files.write(str(result))
    #     # files.close()
    #     code_type = re.findall(r'code_type :(.*)', line)
    #     if (code_type != '[]'):
    #         continue
    #         # if (code_type in list(line)):
    #         files.write(str(code_type))
    # files.close()
