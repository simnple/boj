# May 10, 1981 00:31
# January 01, 2008 00:00
# ([a-zA-Z]+) (\d{2}), (\d{4}) (\d{2}):(\d{2})

import re
import datetime

month = {
    "January": 1,
    "February": 2,
    "March": 3,
    "April": 4,
    "May": 5,
    "June": 6,
    "July": 7,
    "August": 8,
    "September": 9,
    "October": 10,
    "November": 11,
    "December": 12
}

_ = re.search(r"([a-zA-Z]+) (\d{2}), (\d{4}) (\d{2}):(\d{2})", input())

__ = datetime.datetime(int(_.group(3)), 1, 1, 0, 0).timestamp()
___ = datetime.datetime(int(_.group(3)) + 1, 1, 1, 0, 0).timestamp()
____ = datetime.datetime(int(_.group(3)), month[_.group(1)], int(_.group(2)), int(_.group(4)), int(_.group(5))).timestamp()

print((1 - (___ - ____) / (___ - __)) * 100)
