"""
문제
총선이 끝났고 이제 투표를 셀 시간입니다! 후보자 수는 N (2 ≤ N ≤ 5)이고, 투표 지역은 M (1 ≤ M ≤ 100)입니다. 각 후보자에 대해 각 지역에서 얻은 투표 수가 주어졌을 때, 가장 많은 투표를 받은 후보자를 결정하세요.

입력
입력의 첫 번째 줄에는 테스트 케이스의 수 T가 주어집니다.

각 테스트 케이스는 N과 M으로 시작하며, 이는 후보자의 수와 지역의 수를 나타냅니다. 그 다음 M개의 줄에는 각 지역에서 각 후보자가 얻은 투표 수인 N개의 정수(v1, v2, ..., vN)가 주어집니다. (0 ≤ vi ≤ 1000)

출력
각 테스트 케이스에 대해, 승리한 후보자의 번호를 한 줄에 출력하세요. 승자는 유일하다고 가정할 수 있습니다.
"""

# 886
# 1523
# 1840

for _ in range(int(input())):
    __ = list(map(int, input().split(" ")))
    ___ = [list(map(int, input().split(" "))) for ____ in range(__[1])]
    ____ = [0 for _____ in range(__[0])]

    for i in range(__[0]):
        for j in ___:
            ____[i] += j[i]
    
    highest_score = 0
    winner = 0
    for i in range(__[0]):
        if ____[i] > highest_score:
            highest_score = ____[i]
            winner = i + 1

    print(winner)