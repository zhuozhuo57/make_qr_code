from urllib import request


def visit_baidu():
    URL = "https://image.baidu.com/search/index?tn=baiduimage&ps=1&ct=201326592&lm=-1&cl=2&nc=1&ie=utf-8&word=%E5%BF%AB%E9%80%92%E6%9D%A1%E7%A0%81"
    # open the URL
    req = request.urlopen(URL)
    # read the URL
    html = req.read()
    # decode the URL to utf-8
    html = html.decode("utf_8")
    print(html)


if __name__ == '__main__':
    visit_baidu()
