# import time
#
# for i in range(10,0,-1):
#     print(i)
#     time.sleep(1)

# import calendar
#
# def get_week_and_length(year,month):
#     number, length = calendar.monthrange(year,month)
#     print(f"{year}年{month}月一共有{number}个星期和{length}天")
#
# while True:
#     year = int(input("请输入您要查询的年份："))
#     month = int(input("请输入您要查询的月份："))
#     get_week_and_length(year, month)


# 查询某月第一天和最后一天
import calendar
from datetime import date

def get_first_day_and_last_day(year, month):
    week, month_length = calendar.monthrange(year, month)
    first_day = date(year,month,day=1)
    last_day = date(year,month,day=month_length)
    return first_day,last_day

# year = date.today().year
# month = date.today().month
while True:
    year = int(input("请输入您要查询的年份："))
    month = int(input("请输入您要查询的月份："))
    print(get_first_day_and_last_day(year, month))