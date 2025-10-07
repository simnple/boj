# _ = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

# def diff_data(data: list) -> int:
#     days = [_, _]

#     for i in range(2):
#         if data[i][0] % 400 == 0:
#             days[i][1] = 29
        
#         if data[i][0] % 100 != 0:
#             if data[i][0] % 4 == 0:
#                 days[i][1] = 29

#     total_day = 0
#     # same year
#     if data[0][0] == data[1][0]:
#         for i in range(data[0][1], data[1][1] + 1):
#             total_day += days[0][i]
        
#         total_day -= data[0][2]
#         total_day -= days[0][(data[1][1] - 1)] - data[1][2]

#     else:


#     print(total_day)

# diff_data([[2004, 1, 10], [2004, 2, 1]])

# # _ = list(map(int, input().split(" ")))
# # __ = list(map(int, input().split(" ")))
