WORD_AMOUNT = 26

N = int(input())
words = [input() for i in range(N)]

length = [0] * WORD_AMOUNT

for i in range(8, 0, -1):
    for word in words:
        if len(word) >= i:
            idx = ord(word[len(word) - i]) - 65
            length[idx] += 10**(i-1)

sort = sorted(set(length), reverse=True)

num = 9
for i in sort:
    for j in range(WORD_AMOUNT):
        if i == length[j]:
            length[j] *= num
            num -= 1

print(sum(length))