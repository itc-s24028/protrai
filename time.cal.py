#S24028
#カレンダーと今の時刻
import calendar as cal

print(cal.month(2024,6))

import datetime
now = datetime.datetime.now()
print(now)

print(now.strftime("%Y年%m月%d日　%H;%M:%S"))