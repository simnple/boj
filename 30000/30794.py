lv, status = input().split()
lv = int(lv)

result = 0
if status == "miss":
    result = 0
elif status == "bad":
    result = 200 * lv
elif status == "cool":
    result = 400 * lv
elif status == "great":
    result = 600 * lv
elif status == "perfect":
    result = 1000 * lv
print(result)