import sys
import os

lib_path = os.path.abspath(os.path.join(__file__,'..','..','lib'))

sys.path.append(lib_path)

import algorithm

def start():
    n = int(input("Size of n: "))


    show_steps = input('Show steps[y/n]: ')
    if 'y' in show_steps.lower():
        show_steps = True
    else:
        show_steps = False
    
    if n<6: delay = 0.05
    else: delay = 0.005
  


    x = algorithm.init(n,show_steps,delay=delay) 
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