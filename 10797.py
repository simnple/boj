N = int(input())
print(len([i for i in map(int, input().split()) if i == N]))