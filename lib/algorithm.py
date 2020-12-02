import os
import time
clear = lambda: os.system('clear') #Clear terminal

slow_rate = 0.001
def init(n,show_steps=False,delay=0):
    global slow_rate
    slow_rate = delay

    clear()
    x = [-1]*n
    if show_steps == False:
        if solve(0,n,x):
            return x
        return None
    else:
        board = [['_' for j in range(n)] for i in range(n)]
        
        if solve_show_steps(0,n,x,board):
            clear()
            return x
        return None



def solve(k,n,x):
    if (k == n):
        return True
    for i in range(n):
        if place(k,i,x):
            x[k] = i
            if solve(k+1,n,x):
                return True
    
    return False

def solve_show_steps(k,n,x,board):
    if (k == n):
        return True
    for i in range(n):
        if place(k,i,x):
            
            x[k] = i
            board[k][i] = 'X'
            print_board(board)
            if solve_show_steps(k+1,n,x,board):
                return True
            board[k][i] = '_'
            print_board(board)
    
    return False


def place (k,i,x,board = None):
    if board is not None:
        board[k][i] = 'C'
        print_board(board)
        board[k][i] = '_'
        print_board(board)
    for j in range(k):
        if(x[j] == i) or (abs(x[j]-i) == abs(j-k)):
            
            return False
    return True


def print_board(board):
    clear()
    for i in board:
        
        print(" ".join(i))        
        time.sleep(slow_rate)



if __name__ == "__main__":
    print(init(10,True))