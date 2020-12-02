import sys
import os

lib_path = os.path.abspath(os.path.join(__file__,'..','..','lib'))

sys.path.append(lib_path)

import algorithm

def start():
    # n = int(input("Size of n: "))
    n=4
    show_steps = True
    x = algorithm.init(n,show_steps,delay=0.1) 
    if x is None:
        print("board is not solvable")
        return
    print("The solution is ",x)
    for i in x:
        row = ['_' if i!=j else 'X' for j in range(n)]
        row = ' '.join(row)
        print(row)

if __name__ == "__main__":
    start()