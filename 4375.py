while True:
    try:
        n = int(input())

        for i in range(1, 1_000_000):
            if int("1" * i) % n == 0:
                print(len("1" * i))
                break
    except:
        break