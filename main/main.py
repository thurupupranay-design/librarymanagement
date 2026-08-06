import os
import sys

# Add the project root directory to Python's path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from services.library import Library
from utils.input_helper import InputHelper


library = Library()

while True:

    print("\n" + "=" * 40)
    print("     LIBRARY MANAGEMENT SYSTEM")
    print("=" * 40)
    print("1. Add Book")
    print("2. View Books")
    print("3. Register Member")
    print("4. View Members")
    print("5. Issue Book")
    print("6. Return Book")
    print("7. Exit")

    choice = InputHelper.read_int("\nEnter your choice: ")

    if choice == 1:
        book_id = InputHelper.read_int("Enter Book ID: ")
        title = InputHelper.read_string("Enter Book Title: ")
        author = InputHelper.read_string("Enter Author Name: ")

        library.add_book(book_id, title, author)

    elif choice == 2:
        library.view_books()

    elif choice == 3:
        member_id = InputHelper.read_int("Enter Member ID: ")
        name = InputHelper.read_string("Enter Member Name: ")

        library.add_member(member_id, name)

    elif choice == 4:
        library.view_members()

    elif choice == 5:
        member_id = InputHelper.read_int("Enter Member ID: ")
        book_id = InputHelper.read_int("Enter Book ID: ")

        library.issue_book(member_id, book_id)

    elif choice == 6:
        member_id = InputHelper.read_int("Enter Member ID: ")
        book_id = InputHelper.read_int("Enter Book ID: ")

        library.return_book(member_id, book_id)

    elif choice == 7:
        print("\nThank You for Using Library Management System.")
        break

    else:
        print("\nInvalid Choice. Please Try Again.")