from models.person import Person


class Member(Person):
    def __init__(self, person_id, name):
        super().__init__(person_id, name)
        self.borrowed_books = []

    def borrow_book(self, book):
        self.borrowed_books.append(book)

    def return_book(self, book):
        if book in self.borrowed_books:
            self.borrowed_books.remove(book)

    def display(self):
        print(f"\nMember ID : {self.person_id}")
        print(f"Member Name : {self.name}")
        print(f"Books Borrowed : {len(self.borrowed_books)}")

    def __str__(self):
        return f"{self.person_id} - {self.name}"