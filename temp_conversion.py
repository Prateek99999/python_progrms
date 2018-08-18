def temp():
    n = float(input("enter temp."))

    print("enter unit ::  ")
    print()
    a=input("press C --- for °celsius , F --- for °Farehnite and K ---- for kelvin")
    print()
    print(" ________________ ")
    print("enter the unit in which you want to convert input temperature ::")
    print()
    b=input("press C  for °Celsius , F for °Farehnite and K for kelvin")
    print(" ------------------- ")

    a = a.lower()
    b = b.lower()

    if(a=='c' and b=='f'):
        o=n*(9/5)+32
    elif (a == 'c' and b == 'k'):
        o=n+273.15
    elif (a == 'f' and b == 'c'):
        o = (n - 32) * (5 / 9)
    elif (a == 'f' and b == 'k'):
        o = (n + 459.67)*(5 / 9)
    elif (a == 'k' and b == 'f'):
        o = n * (9 / 5) - 459.67
    elif (a == 'k' and b == 'c'):
        o = n - 273.15
    else:
        print("you enterd invalid temperature units::")
        print("plss try again with valid inputs..")

    print(n,"°",a.upper(),"  ---> ",o,"°",b.upper())
temp()

while(1):
    a=input("if you want to continue ,type 'y' else 'n'")
    if(a=='y'):
        temp()
    else:
        print("thank you..")
        break
