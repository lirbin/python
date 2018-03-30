# coding=utf-8
import requests
import json
import sys


class BaiduTranslate:
    def __init__(self):
        self.trans_str = ""
        self.lang_detect_url = "http://fanyi.baidu.com/langdetect"
        self.trans_url = "http://fanyi.baidu.com/basetrans"
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Linux; Android 5.1.1; Nexus 6 Build/LYZ28E) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.84 Mobile Safari/537.36"}

    def parse_url(self, url, data):  # 发送post请求，获取响应
        try:
            response = requests.post(url=url, data=data, headers=self.headers, verify=False)
            # print(json.loads(response.content.decode()))
            return json.loads(response.content.decode())
        except ConnectionError as error:
            return error + '\n网络错误，请重试。'
        except Exception as e:
            return e + '\n出错，请重试。'


    # 翻译方法，参数是原文内容
    def translate(self, trans_str):
        self.trans_str = trans_str
        # 1.获取语言类型
        # 1.1 准备post的url地址，post_data
        lang_detect_data = {"query": self.trans_str}
        # 1.2 发送post请求，获取响应
        lang = self.parse_url(self.lang_detect_url, lang_detect_data)
        # 1.3 提取语言类型
        lang = lang["lan"]
        # 2.准备post的数据
        trans_data = {"query": self.trans_str, "from": "zh", "to": "en"} if lang == "zh" else {
            "query": self.trans_str, "from": "en", "to": "zh"}
        # 3.发送请求，获取响应
        dict_response = self.parse_url(self.trans_url, trans_data)
        # print(dict_response)
        # 4.提取翻译的结果
        # ret = dict_response["trans"][0]["dst"]

        ret = ''
        # 从返回dict中，获取trans，是一个list,包含若干个dict，每个dict中有'dst'键，对应的值为翻译后的内容
        trans = dict_response["trans"]
        for tran in trans:
            ret = ret + tran["dst"] + '\n'
        # print(ret)
        return ret
