import time
def print_board(board):
    # clear()
    for i in board:
        row = ''
        for j in i:
            # print(j)
            print(j,end=' ',flush=True)
            time.sleep(0.1)
        print()

board = [['_' for j in range(4)] for i in range(4)]

print_board(board)