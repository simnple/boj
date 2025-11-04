import sys

input = sys.stdin.readline

def int_to_36(n):
    chars = [str(i) for i in range(10)] + [chr(i) for i in range(65, 91)]
    if n == 0: return n
    result = ""
    while n:
        result += chars[n%36]
        n //= 36
    return result[::-1]

N = int(input())
word_dict = {chr(i): 0 for i in range(65, 91)}
for i in range(10):
    word_dict[str(i)] = 0

char_to_dec = {chr(i): i - 55 for i in range(65, 91)}
for i in range(10):
    char_to_dec[str(i)] = i

nums = {}
for _ in range(N):
    string = input().rstrip()
    can_zero = False
    for i in range(len(string)):
        if string[i] == "0" and (not can_zero and not len(string) - i - 1 == 0): continue
        can_zero = True
        word_dict[string[i]] += 36 ** (len(string) - i - 1)

word_weight = sorted(word_dict, key=lambda x: word_dict[x] * (35 - char_to_dec[x]), reverse=True)

K = int(input())

for i in range(K):
    char_to_dec[word_weight[i]] = 35

total = 0
for key, value in word_dict.items():
    total += value * char_to_dec[key]

print(int_to_36(total))