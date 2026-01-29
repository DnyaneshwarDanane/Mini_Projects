balence = 0

def deposite():
    global balence

    amount = int(input("Enter Amount to deposit: "))
    balence += amount 
    print(f'deposite {amount}. current Balence ={balence}')

def withdraw():
    global balence
    amount = int(input("Enter withdraw amount : "))
    if amount <= balence:
        balence -= amount
        print(f'withdrawn{amount}. Current Balence ={balence} ')
    else:
        print("Ensufficient balence")

def checkbalence():
    print(f'current Balence {balence}')
    

while True:
    print("\n------simple-Bank-System-------")
    print("1.deposite")
    print("2.withdraw")
    print("3.checkbalence")
    print("4.exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
       deposite()

    elif choice == 2:
        withdraw()

    elif choice == 3:
        checkbalence()

    elif choice == 4:
        print("GoodBye")
        break

    else:
        print("invalid choice")




    