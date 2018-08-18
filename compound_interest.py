def ci():
    p=float(input("enter principal amount"))
    r=float(input("enter rate"))
    t=float(input("enter time"))

    a=float(p*((1+r/100)**t))            #a=total amount
    c=float(a-p)                       #c=compound interest
    print("simple interest ::{%0.3f}"%c)

ci()

while(1):
    a=input("if you want to continue ,type 'y' else 'n'")
    if(a=='y'):
        ci()
    else:
        print("thank you..")
        break
