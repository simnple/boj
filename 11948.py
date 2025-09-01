_ = [int(input()) for i in range(6)]

print(sum(sorted(_[:4], reverse=True)[:3]) + sum(sorted(_[4:], reverse=True)[0:1]))