import time
class Demo:
    def arm(self):
        n = int(input("enter  a no."))

        temp = n
        count = 0

        while temp > 0:
            count += 1
            d = temp % 10
            temp //= 10

        # count checks no. of digits in the enterd number

        temp = n
        sum = 0

        while (temp > 0):
            d = temp % 10
            sum += d ** count
            temp //= 10

        if (sum == n):
            print(f"{n} is an armstrong no.")
        else:
            print(f"{n} isn't an armstrong no.")


d=Demo()
d.arm()
while(1):
    a=input("if you want to continue ,type 'y' else 'n'")
    if(a=='y'):
        d.arm()
    else:
        print("ending process")
        time.sleep(5)
        print("------------")

        print("thank you..")
        break
