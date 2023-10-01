T=int(input())

def missing(l):
    x=0
    while True:
        if x in l:
            x+=1
        else:
            return x
        
for i in range (T):
    n=int(input())
    L=list(map(int,input().split()))
    Q=[]
    P=[]
    M=max(L)
    while L:
        for i in range(M+1):
            if i in L:
                if L.count(i)==1:
                    Q.append(i)
                    L.remove(i)
                elif L.count(i)>=2:
                    Q.append(i)
                    P.append(i)
                    L.remove(i)
                    L.remove(i)
                    while i in L:
                        L.remove(i)
                else:
                    pass
            else:
                for i in L:
                    Q.append(i)
                    while i in L:
                        L.remove(i)

    


    print(missing(Q)+missing(P))

    


        
            
