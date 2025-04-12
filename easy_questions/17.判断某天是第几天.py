# 输入某年某月某日，判断这一天是这一年的第几天。
from datetime import datetime
date_str = input('请输入日期，格式为“某年某月某日”：')
dt = datetime.strptime(date_str, '%Y年%m月%d日')
first_day = datetime(dt.year, 1, 1)
day_difference = (dt - first_day).days + 1
print(f'{date_str}是这一年的第{day_difference}天')