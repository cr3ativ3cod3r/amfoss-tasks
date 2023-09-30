try:
    A=input()
    L=len(A)
    x=101
    y=101
    z=101
    r=101
    h=A.index("h")
    if "h" in A:
        for i in range(h+1,L):
            if A[i]=="e":
                x=i
                break
    if "e" in A:
        for j in range(x+1,L):
            if A[j]=="l":
                y=j
                break
    if "l" in A:
        for k in range(y+1,L):
            if A[k]=="l":
                z=k
                break
    if "o" in A:            
        for l in range(z+1,L):
            if A[l]=="o":
                r=l
                break


    if r>z>y>x:
        print("YES")
    else:
        print("NO")
except Exception:
    print("NO")

