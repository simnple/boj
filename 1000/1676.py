N = int(input())

num = 1

for i in range(N, 1, -1):
    num *= i

text = list(str(num))
text.reverse()

count = 0
for i in text:
    if i == "0":
        count += 1
    else: break

print(count)