# -*- coding=utf-8 -*-

'''
 Python3网络爬虫(三)：urllib.error异常
 urllib.error可以接收有urllib.request产生的异常。
 urllib.error有两个方法，URLError和HTTPError
'''
from urllib import request
from urllib import error

if __name__ == "__main__":
    #一个不存在的连接
    url = "http://www.iloveyou.com/"
    req = request.Request(url)
    
    try:
        print('11')
        response = request.urlopen(req)
        html = response.read().decode('utf-8')
        print(html)
    except error.URLError as e:
        print('2')
        print(e.reason)
        
        #[Errno 11002] getaddrinfo failed
        
    #一个不存在的连接
    url = "http://www.douyu.com/Jack_Cui.html"
    req = request.Request(url)
    try:
        responese = request.urlopen(req)
        # html = responese.read()
    except error.HTTPError as e:
        print(e.code)
        print(e.reason)
        
        #403
        #Forbidden