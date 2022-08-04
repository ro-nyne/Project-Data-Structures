from Book import Book
import re

class BookManage(object):

    def __init__(self):
        self.books = []
        self.f = open('BookData.txt', 'r+')
        self.start()

    def start(self):
        str = self.f.readlines()
        lstr = []
        for i in str:
            lstr.append(i.split(','))

        # remove \n from list
        for i in range(len(lstr)):
            for j in range(len(lstr[i])):
                lstr[i][j] = re.sub(r'\n', '', lstr[i][j])

        # append in books
        for i in range(len(lstr)):
            self.books.append(Book(lstr[i][0], lstr[i][1], int(lstr[i][2]), lstr[i][3]))
        # 0: Lend 1: Exist

    def Menu(self):
        self.start()
        while True:
            print("""
                \t|===================================================|
                \t|============ Library management system ============|
                \t|===================================================|
                
        \t1. All books
        \t2. Add books
        \t3. Borrow books
        \t4. Return the book
        \t5. Find location the book
        \t6. Exit the system
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
                self.searchLocation()
            elif choice == '6':
                print('Welcome to use next time...')
                exit()
            else:
                print('Please enter the correct choice')
                continue

    # show all books
    def showAllBook(self):
        for book in self.books:
            print(book)

    # add a book into text file
    def addBook(self):
        name = input('Book name : ')
        author = input('Author : ')
        location = input('storage lacation : ')
        self.books.append (Book (name, author, 1, location))
        self.f.writelines('\n'+name + ',' + author + ',1,' + location)
        print('Book "%s" added successfully'% name)

    # check name of book
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
                self.replacetext(str(name+','+self.searchAuthor(name)+',1'), str(name+','+self.searchAuthor(name)+',0'))
        else:
            print('The book "%s" does not exist'% name)
            

    def returnBook(self):
        name = input('Returned book name : ')
        ret = self.checkBook(name)

        if ret != None:
            if ret.status == 0:
                ret.status = 1
                print('Book "%s" returned successfully'% name)
                self.replacetext(str(name+','+self.searchAuthor(name)+',0'), str(name+','+self.searchAuthor(name)+',1'))
                print(ret)
            else:
                print('The book "%s" has not been lent'% name)
        else:
            print('The book "%s" does not exist'% name)
    
    def searchLocation(self):
        name = input('Book name : ')
        for i in self.books:
            if name == i.name:
                print('Location the book '+name+' is '+ i.bookindex)
                break
        else:
            print('the book "%s" does not exist'% name)
            
    def searchInLine(self, string): 
        indx = 0      
        for line in self.f:
            indx += 1
            
            if string in line:
                return indx
                
    def searchAuthor(self, name):
        for i in self.books:
            if name == i.name:
                return i.author
            
    def sortLacation(self):
        location = []
        for i in self.books:
            location.append(i.bookindex)
        return location
            
    def replacetext(self, search_text, replace_text):
  
        # Opening the file in read and write mode
        with open('BookData.txt','r+') as f:
  
            # Reading the file data and store
            # it in a file variable
            file = f.read()
            
            # Replacing the pattern with the string
            # in the file data
            file = re.sub(search_text, replace_text, file)
    
            # Setting the position to the top
            # of the page to insert data
            f.seek(0)
            
            # Writing replaced data in the file
            f.write(file)
    
            # Truncating the file size
            f.truncate()

        # Return "Text replaced" string
        return "Text replaced"
    # sort book
