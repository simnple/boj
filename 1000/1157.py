import sys

_ = sys.stdin.readline().rstrip()
result = {}

for s in _:
    num = ord(s)
    if num > 96: num -= 32

    if result.get(num) == None:
        result[num] = 0

    result[num] += 1

maximum = 0
maximum_word = ""
for d in result.items():
    if d[1] > maximum:
        maximum = d[1]
        maximum_word = chr(d[0])

if [d[1] for d in result.items()].count(maximum) > 1:
    maximum_word = "?"

print(maximum_word)