class Book:
    def __init__(self, book_id, title, author):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.issued = False

    def issue(self):
        self.issued = True

    def return_book(self):
        self.issued = False

    def __str__(self):
        status = "Issued" if self.issued else "Available"
        return (f"Book ID : {self.book_id}\n"
                f"Title : {self.title}\n"
                f"Author : {self.author}\n"
                f"Status : {status}")