# dp_list를 원래 리스트로 했다가 문자열로 하니 300ms 줄일 수 있었음.

N = int(input())
dp = [0] * (N + 1)
dp_list = [[] for _ in range(N + 1)]

dp[1] = 0
dp_list[1] = "1"

if N > 2:
    dp[3], dp[2] = 1, 1
    dp_list[3], dp_list[2] = "3 1", "2 1"
elif N > 1:
    dp[2] = 1
    dp_list[2] = "2 1"

for i in range(4, N + 1):
    results = [(dp[i - 1] + 1, 0)]
    result_lists = [dp_list[i - 1]]
    if i % 2 == 0:
        results.append((dp[i // 2] + 1, len(results)))
        result_lists.append(dp_list[i // 2])

    if i % 3 == 0:
        results.append((dp[i // 3] + 1, len(results)))
        result_lists.append(dp_list[i // 3])

    dp[i] = min(results)[0]
    dp_list[i] = f"{i} " + result_lists[min(results)[1]]

print(dp[N])
print(dp_list[N])