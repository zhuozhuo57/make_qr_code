# import qrcode
# qr=qrcode.QRCode(version = 2,error_correction = qrcode.constants.ERROR_CORRECT_L,box_size=10,border=10,)
# qr.add_data('http://www.cnblogs.com/sfnz/')
# qr.make(fit=True)
# img = qr.make_image()
# img.show()
# img.save(r'C:\Users\zhangjian\Desktop\QRcode\test.jpg')

import qrcode  # //模块导入

# //调用qrcode的make()方法传入url或者想要展示的内容
img = qrcode.make('http://www.baidu.com')
# //写入文件
with open('../test.png', 'wb') as f:
    img.save(f)
