# input 1 -> 재환
# input 2 -> 의사

# (len ) 비교

__ = [input() for _ in range(2)]

if len(__[0]) >= len(__[1]):
    print("go")
    exit()

print("no")