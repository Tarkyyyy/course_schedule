import time,datetime
now_day = int(time.mktime(datetime.date.today().timetuple())) #获取本日0时时间戳
now_time = int(time.time())
now_date = datetime.date.today()
planTime1 = ['07:30:00','08:10:00','08:20:00','09:00:00','09:25:00','10:05:00','10:15:00','10:55:00','11:00:00','11:40:00']
planTime2 = ['13:30:00','14:10:00','14:20:00','15:00:00','15:15:00','15:55:00','16:05:00','16:45:00','16:45:00','16:20:00']
pp1 = [27000, 29400, 30000, 32400, 33900, 36300, 36900, 39300, 39600, 42000]
pp2 = [48600, 51000, 51600, 54000, 54900, 57300, 57900, 60300, 60300, 58800]
def main():
    for i in planTime2:
      pp2.append(int(time.mktime(time.strptime(str(now_date) + i, '%Y-%m-%d%X')))-now_day)
    print(pp2)
if __name__=="__main__":
    main()