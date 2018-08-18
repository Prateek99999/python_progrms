def evod():
    n=int(input("enter   a  no."))

    if(n%2==0):
        print(f"{n} is an even no.")
    else:
        print(f"{n} is an odd no.")


evod()
while(1):
    a=input("if you want to continue ,type 'y' else 'n'")
    if(a=='y'):
        evod()
    else:
        print("thank you..")
        break
