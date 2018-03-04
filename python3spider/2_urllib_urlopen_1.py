# -*- coding=utf-8 -*-

'''
urlopen的data参数:
    我们可以使用data参数，向服务器发送数据。
    根据HTTP规范，GET用于信息获取，POST是向服务器提交数据的一种请求，再换句话说：

    从客户端向服务器提交数据使用POST；
    从服务器获得数据到客户端使用GET(GET也可以提交，暂不考虑)。
    
    如果没有设置urlopen()函数的data参数，HTTP请求采用GET方式，
    也就是我们从服务器获取信息，如果我们设置data参数，HTTP请求采用POST方式，
    也就是我们向服务器传递数据。
    data参数有自己的格式，它是一个基于application/x-www.form-urlencoded的格式，
    具体格式我们不用了解， 
    因为我们可以使用urllib.parse.urlencode()函数将字符串自动转换成上面所说的格式。
    
'''

from urllib import request
from urllib import parse
import json


if __name__ == '__main__':
    #Request_URL = 'http://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule'
    #去掉_o
    Request_URL = 'http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule'
    
    content = input("输入要翻译的内容：")
    Form_Data = {}
    Form_Data['i'] = content
    Form_Data['doctype'] = 'json'
    #print(Form_Data)
    #'''
    #使用urlencode方法转换标准格式
    data = parse.urlencode(Form_Data).encode('utf-8')
    #print(data)
    response = request.urlopen(Request_URL,data)
    
    html = response.read().decode('utf-8')
    
    #print(html)
    
    #使用JSON
    translate_result = json.loads(html)
    #print(translate_result)
    
    translate_result = translate_result['translateResult'][0][0]['tgt']
    print("翻译的结果是：%s" % translate_result)
    #'''
    
    
    
    