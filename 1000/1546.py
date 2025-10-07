# score*100/M

input()
_ = list(map(int, input().split(" ")))
__ = [__*100 / max(_) for __ in _]
print(sum(__)/len(_))