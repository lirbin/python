# -*- coding=utf-8 -*-

# Cookie，指某些网站为了辨别用户身份、
# 进行session跟踪而储存在用户本地终端上的数据（通常经过加密)。

# http.cookiejar 用本模块的CookieJar类的对象来捕获cookie并在后续连接请求时重新发送
# 比如可以实现模拟登录功能
# 主要的对象有CookieJar、FileCookieJar、MozillaCookieJar、LWPCookieJar

# 工作原理
# 1\建一个带有cookie的opener
# 2\在访问登录的URL时，将登录后的cookie保存下来
# 3\利用这个cookie来访问其他网址。查看登录之后才能看到的信息

# 利用CookieJar对象实现获取cookie的功能

from urllib import request
from http import cookiejar

'''
#  1)将Cookie保存到变量中
if __name__ == '__main__':
    url = 'https://www.csdn.net/'
    # 声明一个CookieJar对象实例来保存cookie
    cookie = cookiejar.CookieJar()
    # 利用urllib.request库的HTTPCookieProcessor对象来创建cookie处理器,
    # 也就是CookieHandler
    handler = request.HTTPCookieProcessor(cookie)
    # 通过CookieHandler创建opener
    opener = request.build_opener(handler)
    opener.addheaders=[('User-Agent', 'Mozilla/5.0 (Linux; Android 4.1.1; Nexus 7 Build/JRO03D) AppleWebKit/535.19 (KHTML, like Gecko) Chrome/18.0.1025.166 Safari/535.19')]
    # 此处的open方法打开网页
    response = opener.open(url)
    # 打印cookie信息
    for item in cookie:
        print('Name = %s' % item.name)
        print('Value = %s' % item.value)

    # 设置保存cookie的文件，同级目录下的cookie.txt
    cookiefile = 'cookie.txt'
    # 声明一个MozillaCookieJar对象实例来保存cookie，之后写入文件
'''
'''
# 2)保存Cookie到文件
if __name__ == '__main__':
    # 设置保存cookie的文件，同级目录下的cookie.txt
    cookiefile = 'cookie.txt'
    # 声明一个MozillaCookieJar对象实例来保存cookie，之后写入文件
    cookie = cookiejar.MozillaCookieJar(cookiefile)
    # 利用urllib.request库的HTTPCookieProcessor对象来创建cookie处理器,
    # 也就是CookieHandler
    handler = request.HTTPCookieProcessor(cookie)
    # 通过CookieHandler创建opener
    opener = request.build_opener(handler)
    url = 'https://www.csdn.net/'

    response = opener.open(url)
    # 保存cookie到文件
    # ignore_discard  :即使cookies将被丢弃也将它保存下来；
    # ignore_expires  :如果在该文件中cookies已经存在，则覆盖原文件写入
    cookie.save(ignore_discard=True,ignore_expires=True)

'''
# 3)从文件中获取Cookie并访问

if __name__ == '__main__':
    # 设置保存cookie的文件的文件名,相对路径,也就是同级目录下
    cookiefile = 'cookie.txt'
    # 创建 MozillaCookieJar对象
    cookie = cookiejar.MozillaCookieJar()
    # 从文件中读取cookie内容到变量
    cookie.load(cookiefile,ignore_expires=True,ignore_discard=True)
    # 利用urllib.request库的HTTPCookieProcessor对象来创建cookie处理器,
    # 也就是CookieHandler
    handler = request.HTTPCookieProcessor(cookie)
    # 通过CookieHandler创建opener
    opener = request.build_opener(handler)
    # 此用opener的open方法打开网页
    url = 'https://www.csdn.net/'
    response = opener.open(url)

    print(response.read().decode('utf-8'))




