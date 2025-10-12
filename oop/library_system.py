class Library:
    def __init__(self, books = [] ):
        self.books = books

    def add_book(self, book):
       self.books.append(book)

    def list_books(self):
        for book in self.books:
            print(book.get_info())
   
   

class Book:
    def __init__(self, title, author):
        self.title = str(title)
        self.author = str(author)

    def get_info(self):
     return f"{self.title} by {self.author}"   
            
    
class EBook(Book):
    def __init__(self, title, author, file_size):
        super().__init__(title, author)
        self.file_size = int(file_size)  # in KB

    def get_info(self):
        return f"{self.title} by {self.author}, File Size: {self.file_size}KB"        


class PrintBook(Book):   
    def __init__(self, title, author, num_pages):
        super().__init__(title, author)
        self.num_pages = int(num_pages)  

    def get_info(self):
     return f"{self.title} by {self.author}, Page Count: {self.num_pages}"   
        