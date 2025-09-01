import math

D, H, W = map(int, input().split())
A = math.sqrt(D**2 / (H**2 + W**2))

print(int(H * A), int(W * A))