n=int(input("enter no. of  terms"))

a=0
d=0
c=1
if(n==1):
    print(a)
elif(n==2):
    print(f"{a} {a+1}")
elif(n>2):
    print(f"{a} {a+1}",end=' ')
    while(d<=n-3):
        b = c + a
        a = c
        c = b
        print(b,end=" ")
        d+=1