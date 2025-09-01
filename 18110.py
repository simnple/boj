import sys

def custom_round(num: float) -> int:
    temp = num - int(num)

    if temp >= 0.5:
        return int(num) + 1
    
    return int(num)

n = int(sys.stdin.readline())

_ = [int(sys.stdin.readline()) for i in range(n)]

_.sort()

remove_count = custom_round(n*0.15)
_ = _[remove_count:len(_) - remove_count]

print(0 if len(_) == 0 else custom_round(sum(_) / len(_)))