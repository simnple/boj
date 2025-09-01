def get_divisions(x):
    divisions = []

    for i in range(1, int(x**(1/2))+1):
        if x % i == 0:
            divisions.append(i)

            if i * i != x and i > 1:
                divisions.append(x // i)
    
    return sorted(divisions)

while True:
    n = int(input())
    if n == -1: break

    divisions = get_divisions(n)
    if sum(divisions) == n:
        print(f"{n} = " + " + ".join(list(map(str, divisions))))
    else:
        print(f"{n} is NOT perfect.")