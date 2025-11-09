N = int(input())
P = int(input())

moneys = [P]
if N >= 5:
    moneys.append(P - 500)
if N >= 10:
    moneys.append(int(P * 0.9))
if N >= 15:
    moneys.append(P - 2000)
if N >= 20:
    moneys.append(int(P * 0.75))

print(max(0, min(moneys)))