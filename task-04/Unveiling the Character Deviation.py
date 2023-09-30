T=int(input())
A="amfoss"
for i in range (T):
    z=0
    b=input()
    for j in range(6):
        a=A[j]
        c=b[j]
        if a!=c:
            z+=1
    print(z)
