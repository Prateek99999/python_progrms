def lc():
    a=int(input("enter first no."))
    b=int(input("enter second no."))

    lcm=0
    x=0

    if(a>b):
        x=a
    else:
        x=b

    while(1):
        if(x%a==0 and x%b==0):
            lcm=x
            break
        x+=1

    print(f"LCM of {a} and {b} is ::{lcm}")

lc()


while(1):
    a=input("if you want to continue ,type 'y' else 'n'")
    if(a=='y'):
        lc()
    else:
        print("thank you..")
        break

