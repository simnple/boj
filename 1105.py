# L R
# L <= x <= R
# x에 8이 가장 적게 들어있는 수에 들어있는 8의 개수

# L, R = input().split(" ")

# count = None
# for i in range(L, R+1):
#     _ = str(i).count("8")
#     if count == None:
#         count = _

#     elif _ < count:
#         count = _

# print(count)

# 8088 8089
# 108 118

L, R = input().split(" ")

count = 0
if len(L) == len(R):
    for i in range(len(L), 0, -1):
        if L[:i] == R[:i]:
            count = L[:i].count("8")
            break

print(count)