def leap():
    n=int(input("enter   an  year"))
    if(n%100==0):
        a=n/100
        if(a%4==0):
            print(f"{n} is a leap year")
        else:
            print(f"{n} isn't a leap year")
    else:
        if(n%4==0):
            print(f"{n} is a leap year")
        else:
            print(f"{n} isn't a leap year")



leap()
while(1):
    a=input("if you want to continue ,type 'y' else 'n'")
    if(a=='y'):
        leap()
    else:
        print("thank you..")
        break
