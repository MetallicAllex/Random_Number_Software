from tkinter import *
import random
class App:
  def __init__(self,master):
    frame = Frame(master)
    frame.pack()
    v = StringVar()
    self.e = Entry(frame,textvariable=v,bd='5')
    v.set('')
    self.v = v
    self.e.pack(padx=5)
    self.button1 = Button(frame,text = 'start',fg='red',command=self.start_hi)
    self.button1.pack(side=LEFT)
    self.button2 = Button(frame,text='stop',fg = 'blue',command=self.say_stop)
    self.button2.pack(side=LEFT)
    self.root=master
    self.stop = 0
    #scrollbar = Scrollbar(frame, orient=VERTICAL)
    #self.b1 = Listbox(frame, yscrollcommand=scrollbar.set)
    #scrollbar.pack(side=RIGHT, fill=Y)
    #self.b1.pack(side=LEFT, fill=BOTH, expand=1)
  def list_star(self):
    star = []
    file = open('yaojiang.txt','r+')
    data = file.readlines()
    file.close()
    for n in data:
      l1 = n.split(':')
      a = l1[0] + ':'+ l1[1][:4] + 'xxxx' + l1[1][8:12]
      a = a.strip()
      star.append(a)
    return star
  def start_hi(self):
    self.stop = 0
    #star = []
    #file = open('yaojiang.txt','r+')
    #data = file.readlines()
    #file.close()
    #for n in data:
      #l1 = n.split(':')
      #a = l1[0] + ':'+ l1[1][:4] + 'xxxx' + l1[1][8:12]
      #a = a.strip()
      #star.append(a)
    star = self.list_star()
    self.update_clock(star)
  def say_stop(self):
    self.stop = 1
    #b = self.start()
  def update_clock(self,star):
    b = random.choice(star)
    self.v.set(b)
    if self.stop == 1:
      return
      self.root.after(50, self.update_clock,star)
root = Tk()
app = App(root)
root.mainloop()