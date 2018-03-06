# -*- coding=utf-8 -*-

'''
使用IP代理:

    (1)调用urlib.request.ProxyHandler()，proxies参数为一个字典。
        class urllib.request.ProxyHandler(proxies=None)
    (2)创建Opener(类似于urlopen，这个代开方式是我们自己定制的)
        urllib.request.build_opener([handler,...])
    (3)安装Opener
        urllib.request.install_opener(opener)
    
    3.代理IP选取
    在写代码之前，先在代理IP网站选好一个IP地址，推荐西刺代理IP。
    URL：http://www.xicidaili.com/
    注意：当然也可以写个正则表达式从网站直接爬取IP，但是要记住不要太频繁爬取，加个延时什么的
    
    编写代码访问http://www.whatismyip.com.tw/，
'''

from urllib import request

if __name__ == '__main__':
    # 该网站是测试自己IP为多少的网址，服务器会返回访问者的IP。
    #url = "http://www.whatismyip.com.tw/"
    url = 'https://www.csdn.net/'
    # 这是代理IP
    proxy = {'http': '49.79.195.82:61234'}
    # 创建ProxyHandler
    proxy_support = request.ProxyHandler(proxies=proxy)
    # 创建Opener
    opener = request.build_opener(proxy_support)
    # 添加User Angent
    opener.addheaders = [('Mozilla/5.0 (Linux; Android 4.1.1; Nexus 7 Build/JRO03D) AppleWebKit/535.19 (KHTML, like Gecko) Chrome/18.0.1025.166 Safari/535.19')]
    # 安装Opener
    request.install_opener(opener)
    # 使用自己安装好的opener
    response = request.urlopen(url)

    html = response.read().decode('utf-8')
    print(html)
