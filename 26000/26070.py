gomgoms = list(map(int, input().split()))
tickets = list(map(int, input().split()))
consume = 0

# 크게 보면 조건문 3개로 while을 거친다.
# - gomgoms[i] and tickets[i]
# 티켓으로 곰곰이를 먹일 수 있는가.
# - gomgoms[(i + 1) % 3] and tickets[i] - gomgoms[i]) // 3
# 티켓을 한번 바꾸고, 그 바꾼 티켓으로 곰곰이를 먹일 수 있는가.
# - gomgoms[(i + 2) % 3] and ((tickets[i] - gomgoms[i]) // 3 + tickets[(i + 1) % 3] - gomgoms[(i + 1) % 3]) // 3
# 티켓을 두번 바꾸고, 그 바꾼 티켓으로 곰곰이를 먹일 수 있는가.

while (gomgoms[0] and tickets[0]) or (gomgoms[1] and tickets[1]) or (gomgoms[2] and tickets[2]) or (gomgoms[1] and (tickets[0] - gomgoms[0]) // 3) or (gomgoms[2] and (tickets[1] - gomgoms[1]) // 3) or (gomgoms[0] and (tickets[2] - gomgoms[2]) // 3) or (gomgoms[2] and ((tickets[0] - gomgoms[0]) // 3 + tickets[1] - gomgoms[1]) // 3) or (gomgoms[0] and ((tickets[1] - gomgoms[1]) // 3 + tickets[2] - gomgoms[2]) // 3) or (gomgoms[1] and ((tickets[2] - gomgoms[2]) // 3 + tickets[0] - gomgoms[0]) // 3):
    for i in range(3):
        if tickets[i] >= gomgoms[i]:
            consume += gomgoms[i]
            tickets[i] -= gomgoms[i]
            gomgoms[i] = 0
        else:
            consume += tickets[i]
            gomgoms[i] -= tickets[i]
            tickets[i] = 0

        rotation_ticket = tickets[i] // 3
        tickets[i] %= 3
        tickets[(i + 1) % 3] += rotation_ticket

print(consume)