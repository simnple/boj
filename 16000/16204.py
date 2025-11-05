# 앞면에 O, X가 적혀있는 카드 N개
# N개의 카드 중 M개의 카드에는 O 한개
# 나머지 카드는 앞면에 X 한개
# 뒷면에 O나 X 적으려고 함.
# O는 K개 X는 N-K개

N, M, K = map(int, input().split())
print(min(M, K) + min(N-M, N-K))