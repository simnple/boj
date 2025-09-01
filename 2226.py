N = int(input())

result = ["1"]

for i in range(N-1):
    temp = []
    for s in result[:]:
        if s == "0":
            temp.append("1")
            temp.append("0")
        elif s == "1":
            temp.append("0")
            temp.append("1")
    
    result = temp

d = "".join(result).split("1")
print(len(d) - d.count(""))