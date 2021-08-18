import logging
import sys

import hubarcode.

logging.getLogger("datamatrix").setLevel(logging.DEBUG)
logging.getLogger("datamatrix").addHandler(logging.StreamHandler(sys.stdout))

if __name__ == "__main__":
    encoder = DataMatrixEncoder(sys.argv[1])
    encoder.save("test.png")
# ————————————————
# 版权声明：本文为CSDN博主「冰炭寒酒」的原创文章，遵循CC
# 4.0
# BY - SA版权协议，转载请附上原文出处链接及本声明。
# 原文链接：https: // blog.csdn.net / sinat_21540191 / article / details / 39758723
