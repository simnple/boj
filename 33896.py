def get_final_score(score, risk, cost):
    return int(score**3 / (cost * (risk + 1)))

n = int(input())
students = {}

for _ in range(n):
    data = input().split()

    name = data[0]
    score, risk, cost = map(int, data[1:])

    students[name] = [cost, get_final_score(score, risk, cost)]

students = sorted(students.items(), key=lambda x: (-x[1][1], x[1][0], x[0]))

print(students[1][0])