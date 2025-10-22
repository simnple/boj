N, M = input().split()

result = ""
A = B = -1

for i in range(2, 37):
    for j in range(2, 37):
        try:
            if int(N, i) == int(M, j):
                if A != -1:
                    result = "Multiple"
                    break
                elif i != j:
                    A = i
                    B = j
                    result = f"{int(N, A)} {A} {B}"
        except: pass

if A == -1:
    result = "Impossible"

print(result)