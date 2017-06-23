import datetime


class Book:
    def __init__(self, isbn, author, title):
        self.isbn = isbn
        self.author = author
        self.title = title

    def equals(self, other_book):
        return self.isbn == other_book.isbn and self.author == other_book.author and self.title == other_book.title

    def __repr__(self):
        return str(self.isbn) + ", " + self.author + ", \"" + self.title + "\""


class LibraryBook(Book):
    def __init__(self, isbn, author, title):
        self.isbn = isbn
        self.author = author
        self.title = title
        self.holder = None
        self.due_date = None

    def set_due_date(self, year, month, day):
        self.due_date = datetime.date(year, month, day)


class Library:
    def __init__(self):
        self.library = []

    def add(self, isbn, author, title):
        self.library.append(LibraryBook(isbn, author, title))

    def add_all(self, book_list):
        for i in book_list:
            self.library.append(i)

    def add_all_from_file(self, file_name):
        with open(file_name) as f:
            for line in f:
                book_desc = line.split(" ")
                self.library.append(LibraryBook(book_desc[0], book_desc[1], book_desc[2]))

    def lookup(self, crit):
        book_list = []
        for i in self.library:
            if isinstance(crit, int):
                if int(i.isbn) == crit:
                    return i  # return the book not just the holder
            else:
                if i.holder == crit:
                    book_list.append(i)
        if len(book_list) != 0:
            return book_list
        return None

    def checkout(self, isbn, holder, month, day, year):
        book = self.lookup(isbn)
        if book is None or book.holder is not None:
            return False
        else:
            book.holder = holder
            book.set_due_date(year, month, day)

    def checkin(self, isbn):
        book = self.lookup(isbn)
        if book is None:
            return False
        else:
            book.holder = None
            book.due_date = None





lib = Library()
lib.add_all_from_file("books.txt")
lib.checkout(134534, "kyle", 11, 22, 1992)
print(lib.lookup(134534), lib.lookup(134534).holder, lib.lookup(134534).due_date)

#theList = [LibraryBook(4, "hey", "there"), LibraryBook(3, "sup", "mang")]
#theList[1].holder = "Tom Hanks"
#lib.add_all(theList)


# lb = LibraryBook(4, "hey", "there")
# lb.set_due_date(1992, 11, 22)
# print(lb.due_date)

# lib = Library()
# lib.add_all_from_file("books.txt")
#
# # lib.add(5, "mike", "meyers")
# # theList = [LibraryBook(4, "hey", "there"), LibraryBook(3, "sup", "mang")]
# # lib.add_all(theList)
# for i in lib.library:
#     print(i.isbn, i.author, i.title)
