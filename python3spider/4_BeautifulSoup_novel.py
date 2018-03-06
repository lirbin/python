# -*- coding=utf-8 -*-

from bs4 import BeautifulSoup
import requests,sys,os


class downloader(object):
    def __init__(self):
        self.server = 'http://www.biqukan.com/'
        self.target = 'http://www.biqukan.com/11_11988/'
        self.names=[]   #存放章节名       
        self.urls=[]    #存放章节链接
        self.nums=0     #存放章节数
        self.curent_path=os.path.split(os.path.abspath(__file__))[0]    #当前目录，或者用os.getcwd()
        self.novel_path=os.path.join(self.curent_path,'novels') #下载后存放的路径
        #print(self.novel_path)
        if not os.path.isdir(self.novel_path):
            os.mkdir(self.novel_path)
            print('创建下载目录：{}'.format(self.novel_path))
        else:
            print('已存在下载目录：{}'.format(self.novel_path))

    def get_urls(self):
        req = requests.get(url=self.target,verify=False) #获取链接的内容
        #html = req.text    #获取html
        bf = BeautifulSoup(req.text,'html.parser')      #bs对象
        div_bf=bf.find_all('div',class_='listmain')     #查找元素
        #print(div_bf[0])
        a_bf = BeautifulSoup(str(div_bf),'html.parser')     #再次获取bs对象
        a = a_bf.find_all('a')
        a = a[12:]                                      #剔除不必要的章节
        self.nums = (len(a))
        for each in a:
            #print(each,each.get('href'))
            self.names.append(each.string)                  #章节名
            #print(each.contents)
            self.urls.append(self.server + each.get('href'))    #章节链接
            #print(each.get('a))    
    
    def get_contents(self,target):
        req = requests.get(url=target,verify=False)
        bf = BeautifulSoup(req.text,'html.parser')
        div_bf = bf.find_all('div',id='content',class_='showtxt')
        contents = div_bf[0].text.replace('\xa0'*8,'\n\n')    #\xa0 是不间断空白符 &nbsp;
        #contents = div_bf[0].text
        return contents
    
    def write(self,path,name,text):
        path=os.path.join(self.novel_path,path)
        wite_flag = True
        with open(path,'a',encoding='utf-8') as f:
            f.write(name + '\n')
            f.writelines(text)
            f.write('\n\n')
        
    
        
        
if __name__ == "__main__":
    dl=downloader()
    dl.get_urls()
    #print(dl.names)
    for i in range(dl.nums):
        dl.write('贞观大闲人.txt',dl.names[i],dl.get_contents(dl.urls[i])) #向文件写入章节名、本章文本
        #sys.stdout.write(" 正在下载：%s" % format(dl.names[i] + '\r'))
        sys.stdout.write(" 已下载:%.3f%%" % float((i/dl.nums)*100) + '\r') #
        sys.stdout.flush()
    print("《贞观大闲人》下载完毕")
        
