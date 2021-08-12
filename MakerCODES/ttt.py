# import qrcode #//模块导入
#  #//调用qrcode的make()方法传入url或者想要展示的内容
# img = qrcode.make('http://www.baidu.com')
# # //写入文件
# with open('test.png', 'wb') as f:
#     img.save(f)

# import qrcode
# import qrcode
# data = 'http://www.baidu.com/'
# img_file = r'C:\Users\zhangjian\Desktop\QRcode\test.jpg'
#
# # 实例化QRCode生成qr对象
# qr = qrcode.QRCode(
#     version=1,
#     error_correction=qrcode.constants.ERROR_CORRECT_H,
#     box_size=10,
#     border=4
# )
# # 传入数据
# qr.add_data(data)
#
# qr.make(fit=True)
#
# # 生成二维码
# img = qr.make_image()
#
# # 保存二维码
# img.save(img_file)
# # 展示二维码
# img.show()


import qrcode

qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)
qr.add_data('test data')
qr.make(fit=True)
img = qr.make_image()
print('img=', img)
img.save('testpng.png')
