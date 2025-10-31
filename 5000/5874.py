data = input()

count = 0
f_leg = 0

for i in range(1, len(data)):
    if data[i-1:i+1] == "((":
        f_leg += 1
    elif data[i-1:i+1] == "))":
        count += f_leg

print(count)