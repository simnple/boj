weight = int(input())

five_kg = weight // 5
three_kg = 0
result = 0

while five_kg:
    three_kg = (weight - five_kg * 5) // 3
    remain = weight - five_kg * 5 - three_kg * 3
    if remain == 0:
        result = five_kg + three_kg
        break
    
    else:
        five_kg -= 1

if result == 0:
    result = weight // 3
    if result * 3 != weight: result = -1

print(result)