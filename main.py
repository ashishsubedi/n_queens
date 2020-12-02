import pprint
import algorithm

def start():
    n = 8
    x = algorithm.init(n) 
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