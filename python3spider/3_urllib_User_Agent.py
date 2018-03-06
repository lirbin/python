# -*- coding=utf-8 -*-

'''
Python3网络爬虫(四)：使用User Agent和代理IP隐藏身份

通过设置User Agent的来达到隐藏身份的目的，
User Agent的中文名为用户代理，简称UA

User Agent存放于Headers中，
服务器就是通过查看Headers中的User Agent来判断是谁在访问

    先看下urllib.request.Request()
    
    class urllib,request.Request(url,data=None,headers={},
    origin_req_host=None,unverrifiable=False,method=None)
    想要设置User Agent，有两种方法：
    1.在创建Request对象的时候，填入headers参数(包含User Agent信息)，这个Headers参数要求为字典；

    2.在创建Request对象的时候不添加headers参数，在创建完成之后，使用add_header()的方法，添加headers。
'''
'''
#方法一

from urllib import request

if __name__ == '__main__':
    url = "http://www.csdn.net/"
    head = {}
    #写入User Agent
    head['User-Agent'] = 'Mozilla/5.0 (Linux; Android 4.0.4; Galaxy Nexus Build/IMM76B) AppleWebKit/535.19 (KHTML, like Gecko) Chrome/18.0.1025.133 Mobile Safari/535.19'
    #创建Request对象
    req = request.Request(url,headers=head)
    #传入创建好的Request对象
    response = request.urlopen(req)
    html = response.read().decode('utf-8')
    print(html)
 
'''
'''
#方法二
from urllib import request


if __name__ == '__main__':
    url = "http://www.csdn.net/"
    req = request.Request(url)
    req.add_header('User-Agent','Mozilla/5.0 (Windows NT 6.2; WOW64; rv:21.0) Gecko/20100101 Firefox/21.0')
    
    response = request.urlopen(req)
    html = response.read().decode('utf-8')
    print(html)
'''



















