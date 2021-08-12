import random
import string

"""
@File:readCase.py
@Description: 描述
@Author:yeqinfang
@Email:yeqinfang@yeah.net
@Date: 2019/08/22
"""

data = {
    "appid": "1",
    "methodname": "add",
    "param": "{\"loginName\":\"yeqinfang013\",\"userPwd\":\"dbb743c87b74802509545a04279a3348\",\"operatorId\":\"117\"}",
    "token": "158ABD2C5A5B4C20A648C0282AA00EC9"
}


def mix_letters(n):
    '''
    :param n: 生成随机数的位数
    :return:返回生成指定数量的随机字符
    '''
    # 随机字符串生成,从a-zA-Z0-9生成指定数量的随机字符
    letters = ''.join(random.sample(string.ascii_letters + string.digits, n))
    return letters


def digits(n):
    '''
    :param n: 生成随机数的位数
    :return:
    '''
    # 随机字符串生成,从0-9生成指定数量的随机数字
    digits = ''.join(random.sample(string.digits, n))
    return digits


def ascii(n):
    '''
    :param n: 生成随机数的位数
    :return:
    '''
    # 随机字符串生成,从a-zA-Z生成指定数量的随机字符
    ascii = ''.join(random.sample(string.ascii_letters, n))
    return ascii


def phone():
    '''
    :param n: 生成随机电话号码
    :return:
    '''
    # 随机字符串生成,从0-9生成指定数量的随机数字
    phone = '136' + ''.join(random.sample(string.digits, 8))
    return phone


if __name__ == "__main__":
    num_str = mix_letters(55)
    print(num_str)
    # print(type(data))
    # print(type(data["param"]))
    # a = data["param"]
    # b = eval(a)
    # print(type(b))
    # # c = b["loginName"]
    # b["loginName"] = num_str
    # print(b)
    # c = data
    # c["param"] = b
    # print(c)
    # print(type(c))
