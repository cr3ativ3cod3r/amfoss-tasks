T=int(input())
def missing(l):
    c=0
    while True:
        if c in l:c+=1
        else:return c
        
for i in range (T):
    n=int(input())
    L=list(map(int,input().split()))
    A=[]
    B=[]
    M=max(L)
    while L:
        for i in range(M+1):
            if i in L:
                if L.count(i)==1:
                    A.append(i)
                    L.remove(i)
                elif L.count(i)==2:
                    A.append(i)
                    B.append(i)
                    L.remove(i)
                    L.remove(i)
                elif L.count(i)>2:
                    A.append(i)
                    B.append(i)
                    while i in L:
                        L.remove(i)
                else:
                    pass
            else:
                for i in L:
                    A.append(i)
                    while i in L:
                        L.remove(i)

    


    print(missing(A)+missing(B))
        
            
