import time,datetime
import data
from tkinter import*
import ctypes
def GetTime():
    global now_date
    global now_day
    global now_time
    global t
    now_day = int(time.mktime(datetime.date.today().timetuple())) #获取本日0时时间戳
    now_time = int(time.time()) - now_day
    now_date = datetime.date.today()
    t = time.localtime()
GetTime()
courseList = []
now_course = 0
labelList = [0,0,0,0,0,0,0,0,0,0]
def GetCourse():
    global courseList
    courseList = data.write(t.tm_wday) #获取本日课表
    
def switch_course(n):
    cout = 0
    if n == 0:
        for i in range(0,9):
            if now_time > data.pp1[i] and now_time < data.pp1[i+1]:
                cout = i + 1
                return cout
        if now_time < data.pp1[0]:
            return 0
        else:
            return 10
    elif n == 1:
        for i in range(0,9):
            if now_time > data.pp2[i] and now_time < data.pp2[i+1]:
                cout = i + 11
                return cout
        if now_time < data.pp2[i]:
            return 10
        else:
            return 20
    else:
        print("error")

root = Tk()
def create():
    global courseList
    global labelList

    # if t.tm_wday == 5:
    #     n = 7
    # else:
    #     n = 10
    for i in range(10):
        labelList[i] = Label(root,text=courseList[i],font=('微软雅黑',17,'bold'),relief=GROOVE,width=8)
        labelList[i].grid(column = 1,row=i)
def dynamic_sh(p):
    n = switch_course(p)
    if n % 2 != 0:
        lb2 = Label(root,text=courseList[int((n-1)/2)],font=('微软雅黑',18,'bold'))
        lb2.grid(column=0,row=4)
        lb1 = Label(root,text='now:',width=8,anchor=W)
        lb1.grid(column=0,row=3)
    else:
        lb2 = Label(root,text=courseList[int(n/2)],font=('微软雅黑',18,'bold'))
        lb2.grid(column=0,row=4)
        lb1 = Label(root,text='next:',width=8,anchor=W)
        lb1.grid(column=0,row=3)
def course_sh(p):
    n = switch_course(p)
    if n % 2 != 0:
        labelList[int((n-1)/2)].config(bg='green')
    elif n != 20:
        labelList[int(n/2)].config(bg='yellow')
def refresh():
    GetTime()
    create()
    if t.tm_hour < 12:
        print(switch_course(0))
        dynamic_sh(0)
        course_sh(0)
    else:
        print(switch_course(1))
        dynamic_sh(1)
        course_sh(1)
    root.update()
    root.after(2000,refresh)
def refresh2():
    GetTime()
    GetCourse()
    print(courseList)
    refresh()  
    
ctypes.windll.shcore.SetProcessDpiAwareness(1)  #告诉操作系统使用程序自身的dpi适配
ScaleFactor=ctypes.windll.shcore.GetScaleFactorForDevice(0) #获取屏幕的缩放因子
root.tk.call('tk', 'scaling', ScaleFactor/75)   #设置程序缩放

root.geometry("220x440+1702+18")
GetCourse()   
create()
root.after(100,refresh)
print(courseList)
bt1 = Button(root,text='11213',command=refresh2)
bt1.grid(column=0,row=9)
root.overrideredirect(True)
# root.attributes('-topmost', True)
root.mainloop()