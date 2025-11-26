balance=10000
while True:
    type=input("enter credit/debit/stop ")
    if(type=='stop'):
        break

    elif(type=='credit'):
        credit_amount = int(input("enter the crediting amount: "))
        balance = balance + credit_amount;
        print(f"The current amount is {balance}")
    elif(type=='debit'):
     debit_amount=int(input("enter the crediting amount: "))
     if(balance>debit_amount):
          balance=balance-debit_amount;
     print(f"The current amount is {balance}")
    else:
        print("error")