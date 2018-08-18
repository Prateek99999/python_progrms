def table():
    n=int(input("enter a no."))

    for a in range(1,11):
        print(a*n)


table()



while(1):
    c=input(" if   you wanna continue , enter 'y' else 'n'")
    if(c=='y'):
        table()
    else:
        print(" ____thank you____ ")
        break

