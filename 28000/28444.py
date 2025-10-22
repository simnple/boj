# 1 -> H*I
# 2 -> A*R*C
# 3 -> 1-2

_ = list(map(int, input().split(" ")))
print(_[0]*_[1] - _[2]*_[3]*_[4])