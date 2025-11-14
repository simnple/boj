max_ppl = 0
currnet_ppl = 0

for _ in range(4):
    quit_train, join_train = map(int, input().split())
    currnet_ppl = currnet_ppl + join_train - quit_train
    max_ppl = max(max_ppl, currnet_ppl)

print(max_ppl)