def large():
    a=int(input(" enter first no. "))
    b=int(input(" enter second no. "))
    c=int(input(" enter third no. "))


    print(f"a : {a} , b : {b} , c : {c}")


    if(a>b):
        if(a>c):
            print(f"{a} is largest")
        else:
            print(f" {b} is largest")
    else:
        if(b>c):
            print(f"{b} is largest")
        else:
            print(f"{c} is largest...")


large()

while(1):
    a=input("if you want to continue ,type 'y' else 'n'")
    if(a=='y'):
        large()
    else:
        print("thank you..")
        break


