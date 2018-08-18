def hc():
    a=int(input("enter first no."))
    b=int(input("enter second no."))

    hcf=0
    x=0

    if(a<b):
        x=a

    else:
        x=b


    for i in range(1,x+1):
        if((a%i)==0 and (b%i)==0):
            hcf=i

    print(f"hcf of {a} and {b} is::",hcf)


hc()

while(1):
    a=input("if you want to continue ,type 'y' else 'n'")
    if(a=='y'):
        hc()
    else:
        print("thank you..")
        break
