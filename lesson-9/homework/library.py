MEMBER_LIMIT = 3

class BookNotFoundException(Exception):
    def __init__(self, book, *args):
        super().__init__(*args)
        self.book = book

    def __str__(self):
        return f"Book '{self.book.title}' not found"

class BookAlreadyBorrowedException(Exception):
    def __init__(self, book, *args):
        super().__init__(*args)
        self.book = book
    def __str__(self):
        return f"Book '{self.book.title}' already borrowed"

class MemberLimitException(Exception):
    def __str__(self):
        return "Your limit fully"

class Book:
    def __init__(self, title, author, is_borrowed=False):
        self.title = title
        self.author = author
        self.is_borrowed = is_borrowed
        Library.books.append(self)
    
    def __str__(self):
        return f"Book({self.title}, {self.author}{', borrowed' if self.is_borrowed else ''})"

class Member:
    def __init__(self, name):
        self.name = name
        self.books = []
    
    def __str__(self):
        return f"Member({self.name})"
    
class Library:
    members = []
    books = []

    @classmethod
    def borrow_book(cls, member: Member, book: Book):
        if book.is_borrowed:
            raise BookAlreadyBorrowedException(book)
        if len(member.books) == MEMBER_LIMIT:
            raise MemberLimitException
        member.books.append(book)
        book.is_borrowed = True
        if not member in cls.members:
            cls.members.append(member)

    @classmethod
    def return_book(cls, member: Member, book: Book):
        if not book in member.books:
            raise BookNotFoundException(book)
        member.books.remove(book)
        book.is_borrowed = False

    @classmethod
    def view_books(cls):
        for book in cls.books:
            print(book)

b1 = Book("Animal farm", "Jorj Oruel")
b2 = Book("Stiv Jobs", "Volter Ayzekson")
b3 = Book("Shaytanat", "Tohir Malik")


u1 = Member("Asadbek")
Library.borrow_book(u1, b3)
Library.view_books()