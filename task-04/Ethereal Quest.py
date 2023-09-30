T=int(input())
a=0
b=0
c=0
l=[]
k=[]
h=[]
for i in range (T):
    x,y,z=map(int,input().split())
    l.append(x)
    k.append(y)
    h.append(z)
for j in range (T):
    a+=l[j]
for v in range(T):
    b+=k[v]
for m in range (T):
    c+=h[m]
    
if a==b==c==0:
    print("YES")
else:
    print("NO")

