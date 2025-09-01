small_kids = [int(input()) for i in range(9)]
total = sum(small_kids)

for i in small_kids:
    for j in small_kids:
        if total - (i + j) == 100 and i != j:
            small_kids.remove(i)
            small_kids.remove(j)
            for k in sorted(small_kids):
                print(k)
            
            exit()