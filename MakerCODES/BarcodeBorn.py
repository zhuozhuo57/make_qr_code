import random
import string

'''pystrich是一个python模块，用于生成1d和2d条码（代码39、代码128、datamatrix、qrcode和ean13）。从hubarcode分叉的。

此包Python名称：pyStrich
目前版本： pyStrich 0.8
最后维护时间：Jul 6, 2016
摘要：PyStrich is a Python module to generate 1D and 2D barcodes (Code 39, Code 128, DataMatrix, QRCode and EAN13). Forked from huBarcode.
安装命令：pip install pyStrich'''
from pystrich.code128 import Code128Encoder
from pystrich.ean13 import EAN13Encoder
from pystrich.code39 import Code39Encoder
from pystrich.datamatrix import DataMatrixEncoder


# from hubarcode.datamatrix import


def makeCode39(n):
    for i in range(n):
        code39str = ''.join(random.sample(string.ascii_uppercase, 10))
        makecode = Code39Encoder(code39str)
        makecode.save(r'C:\Users\zhuoz\Desktop\code39\%s.png' % (code39str))
        print("code39str is ", code39str)


def makecode128(n):
    for i in range(n):
        ran_128 = ''.join(random.sample(string.ascii_letters, 7))
        code = Code128Encoder(ran_128)
        # code.save(r'D:\Workset\barcode\code128\%s.png' %(ran_128))
        code.save(r'C:\Users\zhuoz\Desktop\code128\%s.png' % (ran_128))
        print(ran_128)


def makecodeEAN13(n):
    for i in range(n):
        ran_En13 = ''.join(random.sample(['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '1', '2'], 12))
        # ran_En13 = j
        code = EAN13Encoder(ran_En13)
        print(ran_En13)
        # code.save(r'D:\Workset\barcode\EAN13\%s.png' %(ran_En13))
        code.save(r'C:\Users\zhuoz\Desktop\codeean13\%s.png' % (ran_En13))


def makecodeDataMatrixs(n):
    for i in range(n):
        DataMatrix_code = ''.join((random.sample(string.ascii_uppercase, 10)))
        code = DataMatrixEncoder(DataMatrix_code)
        print(DataMatrix_code)
        code.save(r'C:\Users\zhuoz\Desktop\codedm\%s.png' % (DataMatrix_code))


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    makeCode39(5)
    makecode128(5)
    makecodeEAN13(5)
    makecodeDataMatrixs(5)
