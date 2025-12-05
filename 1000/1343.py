board = input().split(".")

result = []
for s in board:
    if not s:
        result.append("")
    else:
        if len(s) % 2 == 0:
            result.append("AAAA" * (len(s) // 4) + ("BB" if len(s) % 4 else ""))

        else:
            print(-1)
            break

else:
    print(".".join(result))