n = int(input())

sf = tf = f = 0

for i in range(n):
    t, s = map(int, input().split())
    if sf < s:
        sf = s
        tf = t
        f = i + 1

print(tf + (f - 1) * 20 if sf != 0 else 0)