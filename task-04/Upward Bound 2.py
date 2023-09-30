T=int(input())
for i in range (T):
    n=int(input())
    l=list(map(int,input().split()))
    a=l[-1]
    b=0
    if len(l)!=1:
        for j in l[-2::-1]:
            while j>=a:
                j=j//2
                b+=1
                if j==0 and a==0:
                    b=-1
                    break
            a=j
        print(b)
    else:
        print(0)
