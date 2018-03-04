# -*- coding=utf-8 -*-

'''
 Python3网络爬虫(一)：利用urllib进行简单的网页抓取
'''
from urllib import request
import chardet

if __name__ == "__main__":
    response = request.urlopen("http://fanyi.baidu.com")
    html = response.read()
    #print(type(html))   #<class 'bytes'> #二进制
    
    #html = html.decode('utf-8') #解码,此操作需要预先知道该网页的编码方式
    #print(html)
    
    '''
    如果想要自动获取网页的编码方式，可以使用chardet
    pip install chardet   来判断
    
    '''
    
    charset = chardet.detect(html)
    #print(charset)  #{'encoding': 'utf-8', 'confidence': 0.99, 'language': ''}
    
    html = html.decode(charset.get('encoding'))
    print(html)
    