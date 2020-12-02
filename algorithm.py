def init(n):
    x = [-1]*n
    if solve(0,n,x):
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



def place (k,i,x):
    # print(k,i)
    for j in range(k):
        if(x[j] == i) or (abs(x[j]-i) == abs(j-k)):
            return False
    return True
if __name__ == "__main__":
    init()