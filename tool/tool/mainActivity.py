# -*- coding: utf-8 -*-

import tkinter as tk
from tool import translate


class App:
    def __init__(self, window):
        frame = tk.Frame(window)
        frame.pack()

        self.labal_tool = tk.Label(frame, text='百度翻译')
        self.labal_tool.pack()

        #self.scollbar1 = tk.Scrollbar(frame, orient=tk.VERTICAL)
        self.text_src = tk.Text(frame, height=5)
        #self.text_src.configure(yscrollcommand=self.scollbar1.set)
        self.text_src.pack()

        self.btn_tran = tk.Button(frame, text="translate", command=self.btnTranslate)
        self.btn_tran.pack()

        #self.scollbar2 = tk.Scrollbar(frame, orient=tk.VERTICAL)
        self.text_tran = tk.Text(frame, height=8)
        #self.text_src.configure(yscrollcommand=self.scollbar2.set)
        self.text_tran.pack()

        self.translater = translate.BaiduTranslate()

    def btnTranslate(self):
        # 获取待翻译原文的内容，左右去掉空格
        trans_str = self.text_src.get(1.0, tk.END).strip()
        # 判断是否为空或无值
        if trans_str == '' or trans_str == None:
            return

        # 获取译文：调用translater类中的translate方法，参数是原文内容
        text = self.translater.translate(trans_str)
        #
        self.text_tran.delete(1.0, tk.END)
        self.text_tran.insert(1.0, text)
        # text_tran.config(text=text)
        pass


# btn_quit = tk.Button(top,text='QUIT',command=top.quit,activeforeground='white',activebackground='red')  #退出按钮
# btn_quit.pack(fill=tk.X,expand=1)
if __name__ == '__main__':
    top = tk.Tk()  # 根窗口
    top.title('中英文翻译工具')
    # top.geometry('600x600')
    app = App(top)
    tk.mainloop()
