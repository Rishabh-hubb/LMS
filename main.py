class Library:
    def __init__(self,book_list):
        self.book_list = book_list                          # list to store all the books .
        self.library_name = "CountrySide Library"             # name of the library.
        self.lender_dict = {}                              # dictionary to store "book:lender" as key-value pair.

    def displayBooks(self):                                        # display all the books.
        print("Following are the books in our library.")
        for book in self.book_list:
            print(f"Book: {book}")

    def lendBook(self,user,book):                                # to lend book.
        if book not in self.book_list:
            print("Book with that Name Does not exist.")
            print("Please Enter a correct Book name.")
            print("")

        if book not in self.lender_dict.keys():
            self.lender_dict.update({book:user})
        else:
            print("Book has been has been taken by someone")

    def addBook(self,book):                                     # to add books to list of books.
        self.book_list.append(book)
        print("Book has been added to Library.")

    def returnBook(self,book):                                  # return books to library.
        self.lender_dict.pop(book)



obj_1 = Library(["DSA in Python", "Tango with Django", "Dsa in Python", "Python Basics"])


while True:
    print("------------------------CountrySide------------------------")
    print(f"Welcome to {obj_1.library_name} Library. Enter a value to continue")
    print("------------------------###########------------------------")
    print("Type 1. To Display Books")
    print("Type 2. To Lend a Book")
    print("Type 3. To add a Book")
    print("Type 4. To return a Book")
    print("------------------------<><><><><><>------------------------")

    choices = int(input("Enter a number::"))


    if choices == 1:

        obj_1.displayBooks()
    elif choices == 2:
        book = input("Enter the book name you want:")
        name = input("Enter Your name:")

        obj_1.lendBook(book, name)
    elif choices == 3:
        book = input("Enter the name of book You want to add:")
        obj_1.addBook(book)

    elif choices == 4:
        book = input("Enter the name of book You want to return:")
        obj_1.returnBook(book)
    else:
        print("Enter a Valid Option")

    print("Press q to Quit or c to Continue")

    user_choice = ""
    while user_choice != "q" and user_choice != "c":
        user_choice = input("Enter::")
        if user_choice == "q":
            exit()
        elif user_choice == "c":
            continue
        else:
            print("Enter a valid character.")

