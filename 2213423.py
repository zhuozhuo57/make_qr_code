# 检测qr码


# -*- coding: utf-8 -*-
from zxing import BarCodeReader

reader = BarCodeReader()  # 实例化条码读取类
results = reader.decode('3.jpg')  # 调用解码函数进行解码
print(results)  # 打印结果
print('条码类型：', results.format + '\n' +
      '内容类型：', results.type + '\n' +
      '条码内容(raw)：', results.raw + '\n' +
      '条码内容(parsed)：', results.parsed + '\n' +
      '图片路径：' + results.uri + '\n' +
      '坐标点：', results.points  # 实际是二维码定位点的坐标
      )
