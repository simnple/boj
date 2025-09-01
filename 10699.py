# 오늘 날짜

"""
입력
입력은 없다.

출력
서울의 오늘 날짜를 "YYYY-MM-DD" 형식으로 출력한다.
"""

import datetime

KST = datetime.timezone(datetime.timedelta(hours=9))

print(datetime.datetime.now(KST).strftime("%Y-%m-%d"))