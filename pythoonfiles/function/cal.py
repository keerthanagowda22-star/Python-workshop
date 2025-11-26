def userinput():
    f_input=int(input("enter the 1st number:"))
    s_input=int(input("enter the 2nd number"))
    return f_input,s_input

def add(a=0,b=0):
    return a+b

def sub(a=0,b=0):
    return a-b

def multi(a=0,b=0):
    return a*b

print("Calculator")
while True:
    print("select the choose :\n 1.add\n 2.sub\n 3.multi\n 4.stop")
    choose=int(input("enter the choose: "))

    if(choose==1):
        x,y=userinput()
        print(f"addition of 2 number:{add(x,y)}")

    elif (choose == 2):
        x, y = userinput()
        print(f"addition of 2 number:{sub(x, y)}")

    elif (choose == 3):
        x, y = userinput()
        print(f"addition of 2 number:{multi(x, y)}")

    elif (choose == 4):
        print(f"thank you for using calculator")