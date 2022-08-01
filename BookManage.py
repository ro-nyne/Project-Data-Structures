from Book import Book
import re

class BookManage(object):

    def __init__(self):
        self.books = []
        self.f = open('BookData.txt', 'r+')

    def start(self):
        str = self.f.readlines()
        l = []
        for i in str:
            l.append(i.split(','))

        # remove \n from list
        for i in range(len(l)):
            for j in range(len(l[i])):
                l[i][j] = re.sub(r'\n', '', l[i][j])

        for i in range(len(l)):
            self.books.append(Book(l[i][0], l[i][1], int(l[i][2]), l[i][3]))
        # 0: Lend 1: Exist
 
    def Menu(self):
        self.start()
        while True:
            print("""
                ======= Library management system =======
        1. Query books
        2. Add books
        3. Borrow books
        4. Return the book
        5. Exit the system
        """)
 
            choice = input('Please choose : ')
 
            if choice == '1':
                self.showAllBook() #Call the function to display all books
            elif choice == '2':
                self.addBook() #Call the function of adding books
            elif choice == '3':
                self.borrowBook() #Call the function of borrowing books
            elif choice == '4':
                self.returnBook() #Call the function of returning the book
            elif choice == '5':
                print('Welcome to use next time...')
                exit()
            else:
                print('Please enter the correct choice')
                continue
 
    def showAllBook(self):
        for book in self.books:
            print(book)
 
    def addBook(self):
        name = input('Book name : ')
        author = input('Author : ')
        location = input('storage lacation : ')
        self.books.append (Book (name, author, 1, location))
        self.f.writelines('\n'+name + ',' + author + ',1,' + location)
        print('Book "%s" added successfully'% name)

    def checkBook(self, name):
        for book in self.books:
            if book.name == name:
                return book
        else:
            return None

    def borrowBook(self):
        name = input('Name of borrowed book : ')
        ret = self.checkBook(name)
        print(ret)
        #Judge whether the book exists, if it exists, judge whether the book has been lent, if not, borrow it and change its status to 0
        if ret != None:
            if ret.status == 0:   
                print('The book "%s" has been lent'% name)
            else:
                ret.status = 0
                print('Book "%s" borrowed successfully'% name)
        else:
            print('The book "%s" does not exist'% name)
 
    def returnBook(self):
        name = input('Returned book name : ')
        ret = self.checkBook(name)

        if ret != None:
            if ret.status == 0:
                ret.status = 1
                print('Book "%s" returned successfully'% name)
                print(ret)
            else:
                print('The book "%s" has not been lent'% name)
        else:
            print('The book "%s" does not exist'% name)