N = int(input())

_ = [int(input()) for i in range(N)]

print("Junhee is cute!" if sum(_) > N//2 else "Junhee is not cute!")