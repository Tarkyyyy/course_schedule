import time,datetime
import data
from tkinter import*
import ctypes
def GetTime():  #获取时间信息
    global now_date
    global now_day
    global now_time
    global t
    now_day = int(time.mktime(datetime.date.today().timetuple())) #获取本日0时时间戳
    now_time = int(time.time()) - now_day   #当前时间距离0时的秒数
    now_date = datetime.date.today()
    t = time.localtime()
GetTime()
courseList = []
pp1 = []
pp2 = []
now_course = 0
labelList = [0,0,0,0,0,0,0,0,0,0]   #储存Label信息
def GetCourse():    #获取本日课表
    global courseList
    courseList = data.write1(t.tm_wday) 
def GetTable():
    global pp1
    global pp2
    if t.tm_wday != 5:
        pp1 = data.write2(1)
        pp2 = data.write2(2)
    else:
        pp1 = data.write2(3)
        pp2 = data.write2(2)
def switch_course(n):   #判断上下午，并选择课程
    # 课程和课间同时编号，调取时再进行判断
    cout = 0
    if n == 0:
        for i in range(0,9):
            if now_time > pp1[i] and now_time < pp1[i+1]: #判断处于哪一区间
                cout = i + 1
                return cout
        if now_time < pp1[0]: #时间表之外期间
            return 0
        else:
            return 10
    elif n == 1:
        for i in range(0,9):
            if now_time > pp2[i] and now_time < pp2[i+1]:
                cout = i + 11
                return cout
        if now_time < pp2[0]:
            return 10
        else:
            return 20
    else:
        print("error")

root = Tk()
def create():   #创建Label
    global courseList
    global labelList
    for i in range(10):
        labelList[i] = Label(root,text=courseList[i],font=('微软雅黑',24,'bold'),relief=GROOVE,width=8)
        labelList[i].grid(column = 1,row=i)
def dynamic_sh(p):  #实时课程显示
    n = switch_course(p)
    if n % 2 != 0:  #上课期间
        lb2 = Label(root,text=courseList[int((n-1)/2)],font=('微软雅黑',24,'bold'),width=5)
        lb2.grid(column=0,row=4)
        lb1 = Label(root,text='now:',font=('微软雅黑',14,'bold'),width=8,anchor=W)
        lb1.grid(column=0,row=3)
    else:   #课间期间
        lb2 = Label(root,text=courseList[int(n/2)],font=('微软雅黑',24,'bold'),width=5)
        lb2.grid(column=0,row=4)
        lb1 = Label(root,text='next:',font=('微软雅黑',14,'bold'),width=8,anchor=W)
        lb1.grid(column=0,row=3)
def course_sh(p):   #更改Label背景色
    n = switch_course(p)
    if n % 2 != 0:
        labelList[int((n-1)/2)].config(bg='#78E370')
    elif n != 20:
        labelList[int(n/2)].config(bg='#ffdb33')
def refresh():  #循环刷新
    GetTime()
    create()
    n = 0
    if t.tm_hour < 12:
        n = (pp1[switch_course(0)]-now_time)*1000 - 4001
        # print(n)
        dynamic_sh(0)
        course_sh(0)
        # print(switch_course(0))
        # if (switch_course(0) % 2 != 0 and n > 4000) or (switch_course(0)  == 10 and n > 4000) or (switch_course(0) == 0 and n > 4000):
        if  n > 4000:
            root.update()
            root.after(n,refresh)
        else:
            root.update()
            root.after(5000,refresh)
    else:
        # print(switch_course(1))
        n = (pp2[switch_course(1)-10]-now_time)*1000 - 4001
        # print(n)
        dynamic_sh(1)
        course_sh(1)
        if n > 4000:
            root.update()
            root.after(n,refresh)
        else:
            root.update()
            root.after(5000,refresh)
    
def refresh2(): #手动刷新
    GetTime()
    GetCourse()
    GetTable()
    # print(courseList)
    refresh()  
    
# ctypes.windll.shcore.SetProcessDpiAwareness(1)  #告诉操作系统使用程序自身的dpi适配
# ScaleFactor=ctypes.windll.shcore.GetScaleFactorForDevice(0) #获取屏幕的缩放因子
# root.tk.call('tk', 'scaling', ScaleFactor/75)   #设置程序缩放

root.geometry("275x480+1633+12")
root.config(bg="#f4f4f4")
GetCourse()  
GetTable() 
# print(pp1)
create()
root.after(100,refresh)
# print(courseList)
bt1 = Button(root,text='刷新',command=refresh2)
bt1.grid(column=0,row=8)
lb1 = Label(root,text='Designed For Class14')
lb1.grid(column=0,row=9)
root.overrideredirect(True)
# root.attributes('-topmost', True)
root.mainloop()