"""문제
영어 소문자로 이루어진 길이 N의 문자열 S가 주어집니다. S에서 모음의 개수, 즉 a, i, u, e, o의 개수의 합을 구합시다.

입력
아래와 같은 형식으로 표준 입력이 주어집니다.

N
S

출력
S에서 모음의 개수, 즉 a, i, u, e, o의 개수의 합을 출력합니다."""

words = ["a", "i", "u", "e", "o"]
length, word = [input() for _ in range(2)]

count = 0
for w in words:
    count += word.count(w)

print(count)