''' 1. Library System
 
Create a Library class with:
 
*Attributes: books (dict with book title → copies available)
 
*Methods:
 
* borrow(title) → decreases stock if available
 
* return_book(title) → increases stock
 
* show_books() → prints all available books
 
Sample Input:
 
python
 
lib = Library({"Python 101": 3, "Data Science": 2})
 
print(lib.borrow("Python 101"))
 
print(lib.return_book("Python 101"))
 
lib.show_books()
 

 
Sample Output:
 

 
You borrowed Python 101
 
You returned Python 101
 
Available books: {'Python 101': 3, 'Data Science': 2}
 
'''



class Library:
    def __init__(self, books):
        self.books = books
    def borrow(self, title):
        if title in self.books and self.books[title] > 0:
            self.books[title] -= 1
            return "You borrowed", title
        else:
            return "Book not available"
    def return_book(self, title):
        if title in self.books:
            self.books[title] += 1
        else:
            self.books[title] = 1
        return "You returned", title
    def show_books(self):
        print("Available books:", self.books)
lib = Library({"Python 101": 3, "Data Science": 2})
print(lib.borrow("Python 101"))
print(lib.return_book("Python 101"))
lib.show_books()

