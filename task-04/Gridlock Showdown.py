T=int(input())
for i in range(T):
    answer="DRAW"
    x,y,z=map(str,input())
    a,b,c=map(str,input())
    p,q,r=map(str,input())
    if x==y==z or x==b==r or x==a==p:
        answer=x
    elif y==b==q:
        answer=y
    elif z==c==r or z==b==p:
        answer=z
    elif a==b==c:
        answer=a
    elif p==q==r:
        answer=p
    else:
        pass
    
    if answer==".":
        print("DRAW")
    else:
        print(answer)
