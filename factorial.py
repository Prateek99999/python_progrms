import time

def fact():
    n = int(input("enter a no."))

    b = 0
    a = n

    for c in range(n - 1, 1, -1):
        b = a * c
        a = b

    print(f"factorial of {n} is {b}")

fact()


while(1):
    a=input("if you want to continue ,type 'y' else 'n'")
    if(a=='y'):
        fact()
    elif(a=='n'):
        print("closing the progrm...")
        print(" - ",end=" ")
        time.sleep(2)
        print(" - ", end=" ")
        time.sleep(2)
        print(" - ", end=" ")
        time.sleep(2)
        print(" - ",end=" ")
        time.sleep(2)
        print(" - ", end=" ")
        time.sleep(2)
        print(" - ", end=" ")
        time.sleep(2)
        print(" - ", end=" ")
        time.sleep(2)
        print(" - ",)



        print("thank you..")
        break
    else:
        print(" you entered something else")
        print(" we are redirecting you ..")
        time.sleep(3)
        print("ending the progrm....")
        time.sleep(3)
        print(" thank you")
        break

