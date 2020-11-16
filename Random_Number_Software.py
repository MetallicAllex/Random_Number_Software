import tkinter
import tkinter as Tk
from tkinter import Button, Entry, Frame, Label, Menu, Scrollbar, StringVar, Text, messagebox
from tkinter.constants import BOTH, END, RIGHT, Y
from random import randint
from tkinter import *

# 构建窗体
def __init__(self):   
        chuangkou= tkinter()
        chuangkou.title("随机抽取学号") ## 窗体标题
        chuangkou.geometry('800x500') ## 窗体尺寸
# 构建工具栏
    ## “文件”菜单
        menu=Menu(chuangkou)
        submenuwenjian=Menu(menu,tearoff=0)
        submenuwenjian.add_command(label="保存到",command=self.lingcunwei,font=("微软雅黑",12,"normal"))
        menu.add_cascade(label="文件",menu=submenuwenjian,font=("微软雅黑",12,"normal"))
    ## “格式”菜单
        geshi=Menu(menu,tearoff=0)
        geshi.add_command(label="字体",command=self.zitichuang,font=("微软雅黑",12,"normal"))
        menu.add_cascade(label="格式",menu=geshi,font=("微软雅黑",12,"normal"))
    ## 版权菜单
        submenubangzhu=Menu(menu,tearoff=0)
        submenubangzhu.add_command(label="使用说明",command=self.shiyongshuoming,font=("微软雅黑",12,"normal"))
        submenubangzhu.add_command(label="关于",command=self.guanyu,font=("微软雅黑",12,"normal"))
        menu.add_cascade(label="帮助",menu=submenubangzhu,font=("微软雅黑",12,"normal"))
    ## “退出”按钮
        menu.add_command(label="退出",command=chuangkou.quit,font=("微软雅黑",12,"normal"))

        chuangkou.config(menu=menu)
# 构建窗体文本标签
        frame1 = Frame(chuangkou)       
        frame1.pack() 
        zhanghaolabel = Label(frame1, text = "总人数：",font=("微软雅黑",20,"normal"))
        self.name1 = StringVar()
        zhanghaoEntry = Entry(frame1, textvariable = self.name1,font=("微软雅黑",18,"normal"))
        mimalabel = Label(frame1, text = "抽取人数：",font=("微软雅黑",20,"normal"))
        self.name2 = StringVar()
        mimaEntry = Entry(frame1, textvariable = self.name2,font=("微软雅黑",18,"normal"))
        zhucebutton = Button(frame1, text = "随机抽取",font=("微软雅黑",20,"normal"),command = self.chouqu)
        zhanghaolabel.grid(row = 1, column = 1)
        zhanghaoEntry.grid(row = 1, column = 2)        
        mimalabel.grid(row = 2, column = 1)        
        mimaEntry.grid(row = 2, column = 2)
        zhucebutton.grid(row = 3, column = 2)
 
        frame2 = Frame(chuangkou) 
        frame2.pack(fill=BOTH,expand=1) 
        self.xianshibeichouquText=Text(frame2,font=("微软雅黑",24,"bold"))
        self.xianshibeichouquText.pack(fill=BOTH,expand=1)

        gundongtiaoY=Scrollbar(self.xianshibeichouquText)
        self.xianshibeichouquText['yscrollcommand']=gundongtiaoY.set
        gundongtiaoY.pack(side=RIGHT,fill=Y)
        gundongtiaoY.config(command=self.xianshibeichouquText.yview)

        chuangkou.mainloop()
# 构建抽号模块
def chouqu(self,renshu,chouqurenshu):   
        self.xianshibeichouquText.delete(1.0.END)
        liebiao = [ ]
        count=1
        try:
            renshu=int(self.name1.get())
            chouqurenshu=int(self.name2.get())
            if renshu<chouqurenshu:
                chouqurenshu=renshu
        except ValueError:
            tkinter.messagebox.showerror("错误", "请输入整数")
        while count <= chouqurenshu:
            a=randint(1,renshu)
            if a not in liebiao:
                liebiao.append(a)
                count=count+1
        self.xianshibeichouquText.insert(END,"本次共随机抽取"+str(chouqurenshu)+"人\n")
        self.xianshibeichouquText.insert(END,"随机抽到学号如下：\n")
        for b in str(sorted(liebiao)):
            if b != "[" and b!="]" :
                if b==",":
                    self.xianshibeichouquText.insert(END,"号\n")
                else:
                    self.xianshibeichouquText.insert(END,b)  
        self.xianshibeichouquText.insert(END,"号\n")
        liebiao = [ ]   
# 结果存储模块
def lingcunwei(self,filename):
        global f
        f=filename(initialfile="抽取名单.txt",defaultextension=".txt")
        filename=f
        fh=open(f,'w')
        msg=self.xianshibeichouquText.get(1.0,END)
        fh.write(msg)
        fh.close()
# 更改子体模块
def yingyongziti(self):
        self.xianshibeichouquText['font']=(self.zitichosen.get(),self.daxiaochosen.get(),self.getchuandizixing())

def getchuandizixing(self):
        zixing=["常规","normal","粗体","bold","倾斜","italic"]
        self.b="normal"
        for a in enumerate(zixing):
            if self.zixingchosen.get()==a[1]:
                self.b=zixing[a[0]+1]
        return self.b
Tk.mainloop()