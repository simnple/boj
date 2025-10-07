N, S = input().split()
N = int(N)

name = []
count = 0
for i in range(len(S)):
    if S[i] not in name:
        name.append(S[i])
    else:
        count += 1

name = "smupc_" + str(f"{N + 1906}" + "".join(name) + f"{count + 4}")[::-1]
print(name)