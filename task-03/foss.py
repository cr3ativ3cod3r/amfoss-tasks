num=int(input("Enter a number: "))
l=[2]
for i in range(3,num+1):
    a=0
    for j in l:
        if (i%j!=0):
            a+=1
    if a==len(l):
        l.append(i)
        
        
if num>=2:
	print(l)
else:
	print("no primes")
