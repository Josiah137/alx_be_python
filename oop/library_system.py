class Book:  
    def __init__(self, title: str, author: str):  
        """Initialize a Book instance with title and author."""  
        self.title = title  
        self.author = author  

    def __str__(self):  
        """Return string representation of the book."""  
        return f"Book: {self.title} by {self.author}"  

class EBook(Book):  
    def __init__(self, title: str, author: str, file_size: int):  
        """Initialize an EBook instance with title, author, and file size."""  
        super().__init__(title, author)  # Call to the base class constructor  
        self.file_size = file_size  

    def __str__(self):  
        """Return string representation of the ebook."""  
        return f"EBook: {self.title} by {self.author}, File Size: {self.file_size}KB"  

class PrintBook(Book):  
    def __init__(self, title: str, author: str, page_count: int):  
        """Initialize a PrintBook instance with title, author, and page count."""  
        super().__init__(title, author)  # Call to the base class constructor  
        self.page_count = page_count  

    def __str__(self):  
        """Return string representation of the print book."""  
        return f"PrintBook: {self.title} by {self.author}, Page Count: {self.page_count}"  

class Library:  
    def __init__(self):  
        """Initialize the Library with an empty list of books."""  
        self.books = []  

    def add_book(self, book: Book):  
        """Add a Book, EBook, or PrintBook instance to the library."""  
        self.books.append(book)  

    def list_books(self):  
        """Print details of each book in the library."""  
        for book in self.books:  
            print(book)
