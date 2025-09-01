from collections import deque

T = int(input())
for _ in range(T):
    N, M = map(int, input().split())
    document = list(map(int, input().split()))
    queue = deque(range(0,N))
    i_want_to_know_this = queue[M]

    count = 0
    while len(queue) > 0:
        if max(document) == document[queue[0]]:
            count += 1
            document[queue[0]] = 0

            if i_want_to_know_this == queue[0]:
                print(count)
                break
        
        else:
            queue.append(queue[0])

        queue.popleft()