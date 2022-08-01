# Book attributes: book title, author, status, location
# Management system:
class Book(object): #define a book class
 
    def __init__(self, name, author, status, bookindex):
        self.name = name
        self.author = author
        self.status = status
        self.bookindex = bookindex

    def __str__(self):
        if self.status == 1:
            stats ='Not loaned out'
        elif self.status == 0:
            stats ='Already lent'
        else:
            stats ='Status abnormal'
        return 'Title: "% s" Author : % s Status : <% s> location : % s'% (self.name,self.author,self.status,self.bookindex)