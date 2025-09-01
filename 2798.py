# 9 (4)
# 8 7 (4-n) n=1 3
# 7 6 5 (4-n-m) n=1 2

____ = list(map(int, input().split(" ")))[1]
_ = list(map(int, input().split(" ")))
_.sort()
_.reverse()

___ = 0
for i in range(len(_) - 1, -1, -1):
    for j in range(i - 1, -1, -1):
        for k in range(j - 1, -1, -1):
            __ = sum([_[i], _[j], _[k]])
            if ____ >= __:
                if ___ < __:
                    ___ = __
print(___)