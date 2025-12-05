N = int(input())

left_look = 0
left_height = 0

right = []

for _ in range(N):
    height = int(input())

    if left_height < height:
        left_height = height
        left_look += 1
    
    while right and right[-1] <= height:
        right.pop()
    right.append(height)

print(left_look)
print(len(right))