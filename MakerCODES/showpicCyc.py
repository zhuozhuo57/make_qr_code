import glob

import cv2


def main():
    paths = glob.glob(r'D:\Workset\barcode\*.jpg')
    # print(paths)
    imgGo = cv2.imread(r'D:\Workset\Qrcode\Go.jpg')
    cv2.imshow("ReadyGo", imgGo)
    cv2.waitKey(2000)
    for path in paths:
        img = cv2.imread(path)
        cv2.imshow("win", img)
        cv2.waitKey(200)

    cv2.destroyAllWindows()


if __name__ == '__main__':
    main()
