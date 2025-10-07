_ = set([int(input()) for i in range(28)])

for i in sorted(list(set(range(1,31)) - _)):
    print(i)