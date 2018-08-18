def natural():
    n=int(input(" enter  no. of terms"))
    sum=n*(n+1)/2
    print(f" sum of {n} natural no.s   is ::: %d"%sum)


natural()
while(1):
    a=input("if you want to continue ,type 'y' else 'n'")
    if(a=='y'):
        natural()
    else:
        print("thank you..")
        break
