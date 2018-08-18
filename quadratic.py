def quad():
    a=int(input(" enter coefficent a"))
    b=int(input(" enter coefficent b"))
    c=int(input(" enter coefficent c"))



    print(f"a :: {a} , b:: {b} , c::{c}")


    d=(b*b)-(4*a*c)
    if(d>0):
        e=d**0.5
    else:
        e=(-d)**0.5

    if(d>=0):
        print("roots are real")
        s1=(-b+e)/(2*a)
        s2=(-b-e)/(2*a)
        print(f"s1 :: {s1} ")
        print(f"s2 :: {s2} ")
    else:
        print("roots are imagenary")
        u=-b/(2*a)
        v=e/(2*a)
        print(f"s1 :: (%.2f)+(i%.2f)"%(u,v))
        print(f"s2 :: (%.2f)-i(%.2f)"%(u,v))


quad()

while(1):
    a=input("if you want to continue ,type 'y' else 'n'")
    if(a=='y'):
        quad()
    else:
        print("thank you..")
        break
