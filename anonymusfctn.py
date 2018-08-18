def pwr():
    n=int(input("enter the no."))

    power=lambda n :n**3

    print(f"cube of {n} is ",power(n))

pwr()
while(1):
    a=input("if you want to continue ,type 'y' else 'n'")
    if(a=='y'):
        pwr()
    else:
        print("thank you..")
        break




