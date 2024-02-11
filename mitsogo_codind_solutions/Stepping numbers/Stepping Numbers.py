n,m = list(map(int, input("Enter range here: ").split()))
def sub(n):
    L = list(str(n))
    LL = []
    SN = []
    for i in range(0, len(L)):
        if i != len(L)-1:
            a = (int(L[i]) - int(L[i+1])  == 1 or int(L[i]) - int(L[i+1])  == -1)
            LL.append(a)
        else:
            a = (int(L[-2]) - int(L[-1])  == 1 or int(L[-2]) - int(L[-1])  == -1)
            LL.append(a)
    # print(LL)
    if False not in LL:
       print(n, end=" ")

for i in range(n, m):
    sub(i)
