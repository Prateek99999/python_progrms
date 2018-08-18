def prime():
    n=int(input("enter   a  no."))
    t=0

    for a in range(2,(n//2)+1):
        if(n%(a)==0):
            t=1

    if(t==0):
        print(f"{n} is a prime no.")
    else:
        print(f"{n} isn't prime no.")


prime()
while(1):
    a=input("if you want to continue ,type 'y' else 'n'")
    if(a=='y'):
        prime()
    else:
        print("thank you..")
        break
