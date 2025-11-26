balance=10000
bal=int(input("enter the balance: "))
if(bal>=balance):
    print("successfully debited amount")
else:
    print("your amount has been debited")
    bal=balance
    print(f"your new balance {balance} ")