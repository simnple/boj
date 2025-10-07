cal = lambda x: int(x, 2)
_ = map(cal, input().split())
print(bin(sum(_))[2:])
