for i in range(n):
#     for j in range(n):
#         if j == 0:
#             continue
#         if board[i][j - 1] > board[i][j]:
#             is_pass = 1
#             for k in range(j,j + l):
#                 if (board[i][j] != board[i][k]) or (k >= n):
#                     is_pass = 0
#                     break