def swap():
    a=int(input("enter   a"))
    b = int(input("enter  b"))

    print(" before swapping____")
    print(f"a = {a} and b = {b}")

    a=a+b
    b=a-b
    a=a-b

    print(" after swapping____")
    print(f"a = {a} and b = {b}")

swap()
while(1):
    a=input("if you want to continue ,type 'y' else 'n'")
    if(a=='y'):
        swap()
    else:
        print("thank you..")
        break
