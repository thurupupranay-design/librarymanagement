from models.book import Book
from models.member import Member


class Library:
    def __init__(self):
        self.books = []
        self.members = []

    # -------------------- BOOK METHODS --------------------

    def add_book(self, book_id, title, author):
        book = Book(book_id, title, author)
        self.books.append(book)
        print("\n✅ Book Added Successfully!")

    def view_books(self):
        if not self.books:
            print("\nNo Books Available.")
            return

        print("\n========== BOOK LIST ==========")
        for book in self.books:
            print(book)
            print("-" * 30)

    # -------------------- MEMBER METHODS --------------------

    def add_member(self, member_id, name):
        member = Member(member_id, name)
        self.members.append(member)
        print("\n✅ Member Registered Successfully!")

    def view_members(self):
        if not self.members:
            print("\nNo Members Registered.")
            return

        print("\n========== MEMBER LIST ==========")
        for member in self.members:
            member.display()
            print("-" * 30)

    # -------------------- ISSUE BOOK --------------------

    def issue_book(self, member_id, book_id):

        member = None
        book = None

        for m in self.members:
            if m.person_id == member_id:
                member = m
                break

        for b in self.books:
            if b.book_id == book_id:
                book = b
                break

        if member is None:
            print("\nMember Not Found.")
            return

        if book is None:
            print("\nBook Not Found.")
            return

        if book.issued:
            print("\nBook Already Issued.")
            return

        book.issue()
        member.borrow_book(book)

        print("\n✅ Book Issued Successfully!")

    # -------------------- RETURN BOOK --------------------

    def return_book(self, member_id, book_id):

        member = None
        book = None

        for m in self.members:
            if m.person_id == member_id:
                member = m
                break

        for b in self.books:
            if b.book_id == book_id:
                book = b
                break

        if member is None or book is None:
            print("\nInvalid Member or Book.")
            return

        if not book.issued:
            print("\nBook is Already Available.")
            return

        book.return_book()
        member.return_book(book)

        print("\n✅ Book Returned Successfully!")