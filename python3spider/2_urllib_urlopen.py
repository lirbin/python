# -*- coding=utf-8 -*-


'''
Python3网络爬虫(二)：利用urllib.urlopen向有道翻译发送数据获得翻译结果
urllib.request.urlopen的两个重要参数url和data，学习如何发送数据data


url不仅可以是一个字符串，例如:http://www.baidu.com。
    url也可以是一个Request对象，这就需要我们先定义一个Request对象，
    然后将这个Request对象作为urlopen的参数使用，方法如下:
'''

from urllib import request

if __name__ == '__main__':
    req = request.Request("http://www.baidu.com")
    response = request.urlopen(req)
    
    html = response.read().decode('utf-8')
    #print(html)

    '''
     urlopen()返回的对象，可以使用read()进行读取
     同样也可以使用geturl()方法、info()方法、getcode()方法
     
    '''
    # geturl()返回的是一个url的字符串
    url = response.geturl()
    print(url)  #http://www.baidu.com
    
    # info()返回的是一些meta标记的元信息，包括一些服务器的信息；
    meta = response.info()
    print(meta)
    '''
    Date: Sat, 03 Mar 2018 09:33:08 GMT
    Content-Type: text/html; charset=utf-8
    Transfer-Encoding: chunked
    Connection: Close
    Vary: Accept-Encoding
    Set-Cookie: BAIDUID=190A1E527C09F30E00434DD9969613AF:FG=1; expires=Thu, 31-Dec-37 23:55:55 GMT; max-age=2147483647; path=/; domain=.baidu.com
    Set-Cookie: BIDUPSID=190A1E527C09F30E00434DD9969613AF; expires=Thu, 31-Dec-37 23:55:55 GMT; max-age=2147483647; path=/; domain=.baidu.com
    Set-Cookie: PSTM=1520069588; expires=Thu, 31-Dec-37 23:55:55 GMT; max-age=2147483647; path=/; domain=.baidu.com
    Set-Cookie: BDSVRTM=0; path=/
    Set-Cookie: BD_HOME=0; path=/
    Set-Cookie: H_PS_PSSID=1469_21087_17001_20930; path=/; domain=.baidu.com
    P3P: CP=" OTI DSP COR IVA OUR IND COM "
    Cache-Control: private
    Cxy_all: baidu+e2f9b560886374d5ad11850551b6e011
    Expires: Sat, 03 Mar 2018 09:32:54 GMT
    X-Powered-By: HPHP
    Server: BWS/1.1
    X-UA-Compatible: IE=Edge,chrome=1
    BDPAGETYPE: 1
    BDQID: 0xeac6a6fc0001cc95
    BDUSERID: 0
    '''
    # getcode()返回的是HTTP的状态码，如果返回200表示请求成功。
    code = response.getcode()
    print(code) # 200
    
    
    