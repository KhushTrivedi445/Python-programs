class Library:
    def __init__(self):
        self.books = []  
        self.no_of_books = 0
        
    def add_book(self, book_name):
        self.books.append(book_name)
        self.no_of_books += 1

    def print_books(self):
        print("Books in the library:")
        for book in self.books:
            print("-", book)

    def get_number_of_books(self):
        return self.no_of_books



my_library = Library()


my_library.add_book("Rich dad poor dad")
my_library.add_book("Marley and me")
my_library.add_book("Harry potter")

my_library.print_books()

print("Total number of books:", my_library.get_number_of_books())