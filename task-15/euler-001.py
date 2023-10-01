T = int(input())
for i in range (T):
    x=int(input())
    a=0
    for j in range (x):
        if j%3==0 or j%5==0:
            a+=j
    print(a)
