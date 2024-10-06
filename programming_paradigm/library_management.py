class Book:  
    """A class representing a book in the library."""  
    
    def __init__(self, title, author):  
        self.title = title  # Public attribute for book title  
        self.author = author  # Public attribute for book author  
        self._is_checked_out = False  # Private attribute to track availability  

    def check_out(self):  
        """Mark the book as checked out."""  
        if not self._is_checked_out:  
            self._is_checked_out = True  
            return True  
        return False  

    def return_book(self):  
        """Mark the book as available."""  
        if self._is_checked_out:  
            self._is_checked_out = False  
            return True  
        return False  

    def is_available(self):  
        """Check if the book is available."""  
        return not self._is_checked_out  


class Library:  
    """A class representing the library that manages a collection of books."""  
    
    def __init__(self):  
        self._books = []  # Private list to store books  

    def add_book(self, book):  
        """Add a new book to the library."""  
        self._books.append(book)  

    def check_out_book(self, title):  
        """Check out a book by title."""  
        for book in self._books:  
            if book.title == title:  
                if book.check_out():  
                    print(f"You have checked out '{title}'.")  
                    return True  
                else:  
                    print(f"'{title}' is already checked out.")  
                    return False  
        print(f"'{title}' not found in the library.")  
        return False  

    def return_book(self, title):  
        """Return a book by title."""  
        for book in self._books:  
            if book.title == title:  
                if book.return_book():  
                    print(f"You have returned '{title}'.")  
                    return True  
                else:  
                    print(f"'{title}' was not checked out.")  
                    return False  
        print(f"'{title}' not found in the library.")  
        return False  

    def list_available_books(self):  
        """List all available books in the library."""  
        available_books = [book for book in self._books if book.is_available()]  
        
        if available_books:  
            for book in available_books:  
                print(f"{book.title} by {book.author}")  
        else:  
            print("No available books.")
