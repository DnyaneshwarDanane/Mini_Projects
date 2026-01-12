print("-----------Library Management system------------")

librery = {}

while True:
    print("1.Add book")
    print("2.view all books")
    print("3.search book")
    print("4.issue book")
    print("5.return book")
    print("6.exit")

    choice = input("Enter you choice from 1-6: ")

    if choice == "1":
        book = input("Enter your book name: ").strip().lower()
        if book in librery:
            print("book already exits")
        else:
            librery[book] = "Available"
            print("book added successfully")

    elif choice == "2":
        if not librery:
            print("books is not available n\ librery is empty" )

        else:
            print("---n\ librery book ")

            for book ,status in librery.items():
                print(book.title(), "->",status)

    elif choice == "3":
        book = input("Enter the Book Name: ").strip().lower()

        if book in librery:
            print(book.title(),"is",librery[book])

        else:
            print("book not available")

    elif choice == "4":
        book = input("Enter book name: ").strip().lower()

        if book not in librery:
            print("book not available")
        elif librery[book] == "issue":
            print("book already issued")
        else:
            librery[book] = "issue"
            print("book issue successfully")

    elif choice == "5":
        book = input("enter thr book name: ").strip().lower()
        if book not in librery:
            print("book not found")

        elif librery[book] == "issue":  
             print("book was not issued")
        else:
            librery[book] = "Available"
            print("book return successfully")

    elif choice == "6":
        print("exit from process")
        break

    else:
        print("Type valid choice!")















