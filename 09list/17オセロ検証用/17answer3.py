def othello_result(board):
    count_white = sum(row.count('W') for row in board)
    count_black = sum(row.count('B') for row in board)

    if count_white > count_black:
        return "YOU WIN"
    elif count_white < count_black:
        return "YOU LOST"
    else:
        return "EVEN"
othello_board = [input() for _ in range(8)]

result = othello_result(othello_board)
print(result)
