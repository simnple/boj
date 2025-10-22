grade_to_score = {
    "A+": 4.5,
    "A0": 4.0,
    "B+": 3.5,
    "B0": 3.0,
    "C+": 2.5,
    "C0": 2.0,
    "D+": 1.5,
    "D0": 1.0,
    "F": 0.0
}

score = 0
total_score = 0

for _ in range(20):
    lecture_data = input().split()
    if lecture_data[2] == "P": continue

    total_score += float(lecture_data[1])
    score += float(lecture_data[1]) * float(grade_to_score[lecture_data[2]])

print(format(score / total_score, ".6f"))