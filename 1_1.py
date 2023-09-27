import random
g=1
A= [5, 13, 7, 12, 78, 12, 10, 24, 4, 8]
n=len(A)
while g+1!=n:
    c=int((n+g)/2)
    if A[c] % 2 != 0:
        g=c
    elif A[c]%2==0:
        n=c
w=A[n]
print(w)