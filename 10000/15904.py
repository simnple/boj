string = input()

words = ["U", "C", "P", "C"]
idx = 0
result = "I hate UCPC"

for s in string:
    if s == words[idx]:
        idx += 1
    
    if idx == 4:
        result = "I love UCPC"
        break

print(result)