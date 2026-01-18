passwords = []

def load_passwords():
    try:
        with open("password,txt","r") as file:
            for line in file:
                data = line.strip().split(",")
                passwords.append(data)
    except FileNotFoundError:
        pass

def save_password(website,username,password):
    with open("paswords.txt","a") as file:
        file.write(website + "," + username + "," + password +"\n")

load_passwords()

while True:
    print("\n ----Password manager")
    print("1.add pasword")
    print("2.view all password")
    print("3.search password")
    print("4.exit")

    choice = input("Enter your choice: ")

    if choice =="1":
        website = input("Enter website: ")
        username = input("enter username: ")
        password = input("Enter password: ")
        
        passwords.append([website,username,password])

        save_password(website,username,password)

        print("password saved successfully")

    elif choice == "2":
        if not passwords:
            print("no password stored.")

        else:
            for data in passwords:
                print("website: ",data[0])
                print("username: ",data[1])
                print("password: ",data[2])
                print("-" * 20)

    elif choice == "3":
        search_site = input("Enter website to search: ")
        found = False

        for data in passwords:
            if data[0] == search_site:
                print("website: ",data[0])
                print("username: ",data[1])
                print("password: ",data[2])
                found = True
                break

        if not found:
            print("no password found for this wedsite.")

    elif choice == "4":
        print("password manager closed. Goodbye!")
        break
    else:
        print("invalid choice , try again")








