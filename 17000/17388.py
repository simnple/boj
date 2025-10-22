S, K, H = map(int, input().split())

if sum([S, K, H]) < 100:
    if min(S, K, H) == S:
        print("Soongsil")
    elif min(S, K, H) == K:
        print("Korea")
    else:
        print("Hanyang")

else:
    print("OK")