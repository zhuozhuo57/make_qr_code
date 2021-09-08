# 测试一个截取关键字的片段
# 读取LOG日志，截取detect recognition 1:n 比较时间平均值
import sys
from importlib import reload

import numpy as np


def clean_txt(path, ip_addr, n):
    with open(path, 'r') as f:
        lines = f.readlines()
    # print(lines)
    with open(path, 'w') as f_w:
        for line in lines:
            if 'Detect+Recognition' in line:
                continue
            if 'Recognize Face Attr' in line:
                continue
            if 'FaceAttr' in line:
                continue
            if '{' in line:
                continue
            if '}' in line:
                continue
            f_w.write(line)
            try:
                if 'Detect' in line:
                    Detect = line.split('Detect')
                    for str in Detect[1:]:
                        print('str is ' + str)
                        Detect = str.split(' ')
                        print('Detect[1] is %%%%%%%%' + Detect[1])
                        filename = './%s_%d_Detect.txt' % (ip_addr, n)
                        f = open(filename, 'a+')
                        f.write(line + '\n')
                        f.close()
            except:
                print('Get_Detect_Str_Bad')
            try:
                if 'Recognition' in line:
                    Recognition = line.split('Recognition')
                    for str in Recognition[1:]:
                        print('str is ' + str)
                        Recognition = str.split(' ')
                        print('Recognition[1] is %%%%%%%%' + Recognition[1])
                        # filename='./Recognition.txt'
                        filename = './%s_%d_Recognition.txt' % (ip_addr, n)
                        f = open(filename, 'a+')
                        f.write(line + '\n')
                        f.close()
            except:
                print('Get_Recognition_Str_Bad')
            try:
                if 'Compare' in line:
                    Compare = line.split('Compare')
                    for str in Compare[1:]:
                        print('str is ' + str)
                        Compare = str.split(' ')
                        print('Compare[1] is %%%%%%%%' + Compare[1])
                        # filename='./Compare.txt'
                        filename = './%s_%d_Compare.txt' % (ip_addr, n)
                        f = open(filename, 'a+')
                        f.write(line + '\n')
                        f.close()
            except:
                print('Get_Compare_Str_Bad')


def get_performance_Value(path, ip_addr, n):
    with open(path, 'r')as f:
        for line in f.readlines():
            try:
                if 'Detect' in line:
                    Detect = line.split('Detect')
                    for str in Detect[1:]:
                        print('str is ' + str)
                        Detect_value = str.split(' ')
                        print('Detect_value[1] is %%%%%%%%' + Detect_value[1])
                        # filename='./Detect_value.txt'
                        filename = './%s_%d_Detect_value.txt' % (ip_addr, n)
                        f = open(filename, 'a+')
                        f.write(Detect_value[1] + '\n')
                        f.close()
                        avg(filename, ip_addr, n)
            except:
                print('Get_Detect_Str_Bad')
            try:
                if 'Recognition' in line:
                    Recognition = line.split('Recognition')
                    for user in Recognition[1:]:
                        print('user is ' + user)
                        Recognition_value = user.split(' ')
                        print('Recognition_value[1] is %%%%%%%%' + Recognition_value[1])
                        # filename='./Recognition_value.txt'
                        filename = './%s_%d_Recognition_value.txt' % (ip_addr, n)
                        f = open(filename, 'a+')
                        f.write(Recognition_value[1] + '\n')
                        f.close()
                        avg(filename, ip_addr, n)
            except:
                print('Get_Recognition_Str_Bad')
            try:
                if 'Compare' in line:
                    Compare = line.split('Compare')
                    for user in Compare[1:]:
                        print('user is ' + user)
                        Compare_value = user.split(' ')
                        print('Compare_value[1] is %%%%%%%%' + Compare_value[1])
                        # filename='./Compare_value.txt'
                        filename = './%s_%d_Compare_value.txt' % (ip_addr, n)
                        f = open(filename, 'a+')
                        f.write(Compare_value[1] + '\n')
                        f.close()
                        avg(filename, ip_addr, n)
            except:
                print('Get_Compare_Str_Bad')


def avg(path, ip_addr, n):
    count = 0
    reload(sys)
    sys.setdefaultencoding('utf-8')
    result = u'累加全部数值为：'
    str = ip_addr + n
    avgs = u'平均值为：'
    with open(path, 'r') as f:
        for line in f:
            # print ('line is '+line.strip('.'))
            score = float(line)
            # sum=int(score)
            avg = np.mean(score)
        print(str + avgs + bytes(avg) + 'ms')


if __name__ == "__main__":
    get_performance_Value(path)
    clean_txt(path, ip_addr, n)
    # avg('./Detect_value.txt','Detect')
    # avg('./Recognition_value.txt','Recognition')
    # avg('./Compare_value.txt','Compare')
    # aaa('32linux.txt')
