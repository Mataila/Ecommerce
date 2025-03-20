class Book:
    def __init__(self, title, author, publication_year):
        """
        Initialize a Book object with title, author, and publication year.
        The book is initially not borrowed.
        """
        self.title = title
        self.author = author
        self.publication_year = publication_year
        self.borrowed = False
    
    def borrow_book(self):
        """Marks the book as borrowed if it is not already borrowed."""
        if not self.borrowed:
            self.borrowed = True
            print(f'The book "{self.title}" has been borrowed.')
        else:
            print(f'The book "{self.title}" is already borrowed.')
    
    def return_book(self):
        """Marks the book as returned if it is currently borrowed."""
        if self.borrowed:
            self.borrowed = False
            print(f'The book "{self.title}" has been returned.')
        else:
            print(f'The book "{self.title}" was not borrowed.')
    
    def display_info(self):
        """Displays the book's details including title, author, publication year, and borrowed status."""
        status = "Borrowed" if self.borrowed else "Available"
        print(f'Title: {self.title}, Author: {self.author}, Year: {self.publication_year}, Status: {status}')

# Example usage
if __name__ == "__main__":
    book1 = Book("The Great Gatsby", "F. Scott Fitzgerald", 1925)
    book1.display_info()
    book1.borrow_book()
    book1.display_info()
    book1.return_book()
    book1.display_info()
