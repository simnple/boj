def is_vowel(s):
    return s in ["a", "e", "i", "o", "u"]

def backtracking():
    global vowels, curr_idx
    if len(result) == L:
        print("".join(result))
        return
    
    else:
        last_idx = curr_idx + 1
        for i in range(last_idx, C):
            if visited[i]: continue

            vowel_check = is_vowel(S[i])
            # 모음 선택 안하는 기준
            # L - vowels가 2보다 작으면 선택 안함
            if L - vowels <= 2 and vowel_check: continue
            # 자음 선택 안하는 기준
            # L - len(result)가 1인데 vowels == 0이면
            if L - len(result) == 1 and vowels == 0 and not vowel_check: continue
            if L - len(result) > C - i: break

            if vowel_check: vowels += 1
            result.append(S[i])
            visited[i] = 1
            curr_idx = i

            backtracking()

            if vowel_check: vowels -= 1
            result.pop()
            visited[i] = 0
            curr_idx = last_idx

L, C = map(int, input().split())
S = sorted(input().split())

visited = [0] * C
vowels = 0
curr_idx = -1
result = []

backtracking()