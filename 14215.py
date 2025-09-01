side_length = list(map(int, input().split()))
left_side_length = side_length[:]
left_side_length.remove(max(side_length))

if sum(left_side_length) > max(side_length):
    print(sum(side_length))
else:
    print(sum(left_side_length) + sum(left_side_length)-1)