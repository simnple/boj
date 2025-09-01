members = [input().split() for _ in range(3)]
first_way = "".join([str(int(i[1])%100) for i in sorted(members, key=lambda x: int(x[1]))])
second_way = "".join([i[2][0] for i in sorted(members, key=lambda x: -int(x[0]))])

print(first_way, second_way, sep="\n")