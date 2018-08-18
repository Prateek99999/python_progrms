def si():
    p=float(input("enter principal amount"))
    r=float(input("enter rate"))
    t=float(input("enter time"))

    s=(p*r*t)/100

    print("simple interest ::{%0.3f}"%s)

si()

while(1):
    a=input("if you want to continue ,type 'y' else 'n'")
    if(a=='y'):
        si()
    else:
        print("thank you..")
        break
