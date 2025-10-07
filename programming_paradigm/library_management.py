class Book:
    def __init__(self,title, author):
        self.title = title
        self.author = author
        self._is_checked_out = False




class Library:    
    def __init__(self):
        self.books = []

    def add_book(self,book):
        self.books.append(Book) 


    def check_out_book(self,book):
        
        if book in self.books and not Book._is_checked_out:
            Book._is_checked_out = True
            return True
        return False    

    def return_book(self, book):
        
        if book in self.books and Book._is_checked_out:
            Book._is_checked_out = False
            return True
        return False    

    def list_available_books(self):
        available_books = [book for book in self.books if not book._is_checked_out]
        for book in available_books:
            print(f"{book.title} by {book.author}")
        return available_books