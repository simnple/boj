input()
_ = map(int, input().split(" "))

__ = 0
for ___ in _:
    if ___ <= 1:
        continue

    for i in range(2, ___):
        if ___ % i == 0:
            break
    
    else:
        __ += 1

print(__)