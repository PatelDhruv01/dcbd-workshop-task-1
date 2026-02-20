def fibHelp(i, F):
    if F[i]!=0:
        return F[i]
    f1 = fibHelp(i-1, F)
    f2 = fibHelp(i-2, F)
    return f1+f2


def fibo(n):
    if n<=1:
        return 1
    F = [0 for i in range(n+1)]
    F[0]=1
    F[1]=1
    return fibHelp(n, F)

# print(fibo(5))