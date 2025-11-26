age=int(input("enter the age: "))
def vote(age):
    if(age<18):
        print("not eligible")
    elif(age>18):
        print("eligible")