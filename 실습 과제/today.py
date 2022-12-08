from calendar import day_abbr, weekday
from datetime import datetime

today = datetime.today()
weekday = today.weekday()
week=""
if weekday == 0:
    week = "월"
elif weekday == 1:
    week = "화"
elif weekday == 2:
    week = "수"
elif weekday == 3:
    week = "목"
elif weekday == 4:
    week = "금"
elif weekday == 5:
    week = "토"
elif weekday == 6:
    week = "일"

print("오늘은",today.year,"년",today.month,"월",today.day,"일",week,"요일입니다")