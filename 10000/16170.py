# 그냥 "0" 추가함

from datetime import datetime

_ = datetime.today()

print(_.year)
print("0"+str(_.month))
print("0"+str(_.day))