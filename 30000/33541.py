def is_special(x):
    x = str(x)
    a, b = map(int, [x[:2], x[2:]])
    return (a + b)**2 == int(x)

X = int(input())

result = -1
for i in range(X+1, 10000):
    if is_special(i):
        result = i
        break
print(result)