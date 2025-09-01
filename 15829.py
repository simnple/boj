# - 96
input()
_ = input()
___ = 0
for i in range(len(_)):
    __ = ord(_[i]) - 96
    ___ += __ * 31**i
print(___ % 1234567891)