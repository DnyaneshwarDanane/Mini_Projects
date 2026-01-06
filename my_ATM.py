print("welcome to ATM")

pin = 0000
balance = 1700

enterd_pin = int(input("Enter your pin: "))

if enterd_pin == pin:
    print("Login successfull!")

    while True:
        print("\n-------ATM Menu--------- ")
        print("1.check current balence")
        print("2.Withdraw money")
        print("3.Diposit money")
        print("4.exit")

        choice = int(input("Enter your choice: "))

        if choice == 1:
            print("check current balance: ",balance)

        elif choice == 2:
            amount = int(input("Enter withdrawal amount: "))
            if amount <= balance:
                print("withdrawal successful")
                balance-=amount
                print("updated amount",balance)
            
            else:
                print("inefficiant balance ")

        elif choice == 3:
            amount = int(input("Enter amount to add in balance : "))

            balance+=amount

            print("updated balance",balance)

        elif choice == 4:
            print("exit from ATM")
            break
else:
    print("invalid pin")

    