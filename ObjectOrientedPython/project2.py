import sys


# Code Start:

class Library:
    def _init_(self, Name):
        self.Name = Name


Library._name_ = '     The Library of Congress'
print('-----------------------------------')
print(Library._name_)
print('-----------------------------------')

Choice = ''


class User:
    def _init_(self, Username, Password):
        self.Username = Username
        self.Password = Password


    while True:
        print('Login: [L] \nGuest: [G]')
        print('-----------------------------------')
        Choice = input('Enter: ').lower()
        if Choice == 'l':
            print('-----------------------------------')
            Username = input('Enter your Username: ')
            Password = input('Enter your Password: ')
            print('-----------------------------------')
            print('-----------------------------------')
            Hide = '*' * len(Password)
            print(f'Username: [{Username}] \nPassword: {Hide}')
            print('-----------------------------------')
            break


        elif Choice == 'g':
            print('-----------------------------------')
            print('-----------------------------------')
            print('Welcome Guest!')
            print('-----------------------------------')
            break

        else:
            print('-----------------------------------')
            print('Invalid Input.')
            print('-----------------------------------')
            continue


class Book:
    def _init_(self, Name, Author, ISBN):
        self.Name = Name
        self.Author = Author
        self.ISBN = ISBN



library = []

name = ''
author = ''
isbn = ''



while True:
    print('-----------------------------------')
    print('◯ Add New Book:         [1]\n◯ Check Availability:   [2]\n◯ Delete Book:          [3]\n◯ List of the Books:'
          '    [4]\n◯ Exit:                 [5]')
    print('-----------------------------------')

    Command = input('Enter a Command: ').lower()

    if Command == '1':

        name = input("Enter the Book's Title: ").lower()
        author = input("Enter the Book's Author: ").lower()
        isbn = input("Enter the Book's ISBN: ").lower()

        while any(book.Name.lower() == name.lower() for book in library):
            print('-----------------------------------')
            print('A Book with this Name already exists.')
            print('-----------------------------------')
            name = input("Enter the Book's Title: ").lower()

        while any(book.ISBN.lower() == isbn.lower() for book in library):
            print('-----------------------------------')
            print('A Book with this ISBN already exists.')
            print('-----------------------------------')
            isbn = input("Enter the Book's ISBN: ").lower()

        book = Book(name, author, isbn)
        library.append(book)
        print('-----------------------------------')
        print('Book Added Successfully!')
        print('-----------------------------------')


    elif Command == '2' and Library:
        BookName = input("Enter the Name of the Book: ").lower()
        AvailableBook = next((Book for Book in library if BookName.lower() == name))
        if AvailableBook:
            print('-----------------------------------')
            print(f"The Book '[{BookName.title()}]' is Available.")
            print('-----------------------------------')
            print("Information: ")
            print(f"Name: {name.title()}")
            print(f"Name: {author.title()}")
            print(f"Name: {isbn.title()}")
        else:
            print('-----------------------------------')
            print(f"The Book '[{BookName.upper()}]' is NOT Available.")

    elif Command == '3':
        BookName = input("Enter the Name of the Book: ").lower()
        DeletedBook = [Book for Book in library if name == BookName]
        if DeletedBook:
            library.remove(DeletedBook[0])
            print('-----------------------------------')
            print(f"The book [{BookName.upper()}] has been deleted.")
        else:
            print('-----------------------------------')
            print(f"The book [{BookName.upper()}] does NOT exist in the Library.")


    elif Command == '4':
        TotalBooks = len(library)
        print('-----------------------------------')
        print(f'Total Number of Books: {TotalBooks}')
        if TotalBooks != 0:
            print(f'The Books: ')
        for book in library:
            print(f"◯'{book.Name.title()}' by the Author '{book.Author.title()}' [{book.ISBN}]")


    elif Command == '5':
        print('-----------------------------------')
        print('-----------------------------------')
        print("Thank you for using this Software")
        print('-----------------------------------')
        sys.exit()

    else:
        print('-----------------------------------')
        print('Invalid Command!')
        continue


class Information:
    def _init_(self, Title, Author, ISBN):
        self.Title = Title
        self.Author = Author
        self.ISBN = ISBN

    class Fine:
        def _init_(self, CurrentDate, FineAmount):
            self.CurrentDate = CurrentDate
            self.FineAmount = FineAmount

    class Return:
        def _init_(self, Username, ISBN, ReturnDate, Rating):
            self.Username = Username
            self.ISBN = ISBN
            self.ReturnDate = ReturnDate
            self.Rating=Rating
