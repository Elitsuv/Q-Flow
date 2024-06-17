L = [5,10,15,1]
G = 4
def Change(X):
    global G
    N=len(X)
    for i in range(N):
     X[i] += G
Change(L)
for i in L:
 print(i,end='$')