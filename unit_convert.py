
def convert():
    cat = input("what would you like to convert?  length(l) or Weight(w) or time(t):  ")
    if cat == ("l"):
        print("Which unit would you like to convert from: ------")
        unit1 = input("enter cm or m or mm or km")
        print()
        print("Which unit would you like to convert to: ")
        unit2 = input("enter cm or m or mm or km")
        print()

        num1 = input("Enter your value: ")

        ##Calculations

        if unit1 == "cm" and unit2 == "m":
            ans = float(num1) / 100
            print(f"{num1} cm ---> {ans} m")
        elif unit1 == "cm" and unit2 == "mm":
            ans = float(num1) * 10
            print(f"{num1} cm ---> {ans} mm")

        elif unit1 == "cm" and unit2 == "km":
            ans = float(num1) / 100000
            print(f"{num1} cm ---> {ans} km")


        elif unit1 == "mm" and unit2 == "cm":
            ans = float(num1) / 10
            print(f"{num1} mm ---> {ans} cm")

        elif unit1 == "mm" and unit2 == "m":
            ans = float(num1) / 1000

            print(f"{num1} mm ---> {ans} m")

        elif unit1 == "mm" and unit2 == "km":
            ans = float(num1) / 1000000
            print(f"{num1} mm ---> {ans} km")



        elif unit1 == "m" and unit2 == "cm":
            ans = float(num1) * 100
            print(f"{num1} m ---> {ans} cm")


        elif unit1 == "m" and unit2 == "mm":
            ans = float(num1) * 1000
            print(f"{num1} m ---> {ans} mm")


        elif unit1 == "m" and unit2 == "km":
            ans = float(num1) / 1000
            print(f"{num1} m ---> {ans} km")


        elif unit1 == "km" and unit2 == "m":
            ans = float(num1) * 1000
            print(f"{num1} km ---> {ans} m")


        elif unit1 == "km" and unit2 == "cm":
            ans = float(num1) * 100000
            print(f"{num1} km ---> {ans} cm")

        elif unit1 == "km" and unit2 == "mm":
            ans = float(num1) * 10000000
            print(f"{num1} km ---> {ans} mm")


    elif cat == ("t"):
        print("Which unit would you like to convert from: ")
        unit1 = input("enter  s for second or m for minute or h for hour")
        print("Which unit would you like to convert to: ")
        unit2 = input("enter  s for second or m for minute or h for hour")
        num1 = input("Enter your value: ")

        if unit1 == "s" and unit2 == "h":
            ans = float(num1) / 3600
            print(f"{num1} s ---> {ans} hrs")

        elif unit1 == "s" and unit2 == "m":
            ans = float(num1) / 60
            print(f"{num1} s ---> {ans} mins")

        elif unit1 == "m" and unit2 == "h":
            ans = float(num1) / 60
            print(f"{num1} min ---> {ans} hrs")

        elif unit1 == "m" and unit2 == "s":
            ans = float(num1) * 60
            print(f"{num1} min ---> {ans} s")

        elif unit1 == "h" and unit2 == "m":
            ans = float(num1) * 60
            print(f"{num1} hrs ---> {ans} min")

        elif unit1 == "h" and unit2 == "s":
            ans = float(num1) * 3600
            print(f"{num1} hrs ---> {ans} s")



    elif cat == ("w"):
        print("Which unit would you like to convert from: ")
        unit1 = input("enter  kg  or g  or lbs or p for pound")
        print("Which unit would you like to convert to: ")
        unit2 = input("enter  kg  or g  or p for pound")
        num1 = input("Enter your value: ")

        if unit1 == "kg" and unit2 == "g":
            ans = float(num1) * 1000
            print(f"{num1} kg ---> {ans} g")

        elif unit1 == "kg" and unit2 == "p":
            ans = float(num1) * 2.204
            print(f"{num1} kg ---> {ans} lbs")

        elif unit1 == "g" and unit2 == "p":
            ans = float(num1) * .00205
            print(f"{num1} g ---> {ans} lbs")

        elif unit1 == "g" and unit2 == "kg":
            ans = float(num1) / 1000
            print(f"{num1} g ---> {ans} kg")

        elif unit1 == "p" and unit2 == "kg":
            ans = float(num1) * .453
            print(f"{num1} lbs ---> {ans} kg")


        elif unit1 == "p" and unit2 == "g":
            ans = float(num1) * 453.59
            print(f"{num1} lbs ---> {ans} g")





convert()


while(1):
    a=input("if you want to continue ,type 'y' else 'n'")
    if(a=='y'):
        convert()
    else:
        print("thank you..")
        break



