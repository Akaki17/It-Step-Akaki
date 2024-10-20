from models import Book

# Add New Book
def add_book(title, author, release_year, isbn):
    new_book = Book(title=title, author=author, release_year=release_year, isbn=isbn)
    session.add(new_book)
    session.commit()
    print(f"Book '{title}' added successfully.")

# Read All Books
def read_all_books():
    books = session.query(Book).all()
    if books:
        for book in books:
            print(f"Title: {book.title}, Author: {book.author}, Year: {book.release_year}, ISBN: {book.isbn}")
    else:
        print("No books found in the database.")

# Search Book by ISBN
def search_book_by_isbn(isbn):
    book = session.query(Book).filter_by(isbn=isbn).first()
    if book:
        print(f"Title: {book.title}, Author: {book.author}, Year: {book.release_year}, ISBN: {book.isbn}")
    else:
        print(f"No book found with ISBN: {isbn}")

# Update Book Details
def update_book_details(isbn, title=None, author=None, release_year=None):
    book = session.query(Book).filter_by(isbn=isbn).first()
    if book:
        if title:
            book.title = title
        if author:
            book.author = author
        if release_year:
            book.release_year = release_year
        session.commit()
        print(f"Book with ISBN {isbn} updated successfully.")
    else:
        print(f"No book found with ISBN: {isbn}")

# Delete Book
def delete_book(isbn):
    book = session.query(Book).filter_by(isbn=isbn).first()
    if book:
        session.delete(book)
        session.commit()
        print(f"Book with ISBN {isbn} deleted successfully.")
    else:
        print(f"No book found with ISBN: {isbn}")
def menu():
    while True:
        print("\n=== Book Management System ===")
        print("1. Add a New Book")
        print("2. Read All Books")
        print("3. Search Book by ISBN")
        print("4. Update Book Details")
        print("5. Delete a Book")
        print("6. Exit")
        
        choice = input("Enter your choice (1-6): ")
        
        if choice == '1':
            title = input("Enter book title: ")
            author = input("Enter author name: ")
            release_year = int(input("Enter release year: "))
            isbn = input("Enter ISBN: ")
            add_book(title, author, release_year, isbn)
        
        elif choice == '2':
            read_all_books()
        
        elif choice == '3':
            isbn = input("Enter ISBN to search: ")
            search_book_by_isbn(isbn)
        
        elif choice == '4':
            isbn = input("Enter ISBN to update: ")
            title = input("Enter new title (or press Enter to keep current): ")
            author = input("Enter new author (or press Enter to keep current): ")
            release_year = input("Enter new release year (or press Enter to keep current): ")
            update_book_details(isbn, title=title if title else None, author=author if author else None, release_year=int(release_year) if release_year else None)
        
        elif choice == '5':
            isbn = input("Enter ISBN to delete: ")
            delete_book(isbn)
        
        elif choice == '6':
            print("Exiting the program.")
            break
        
        else:
            print("Invalid choice. Please try again.")

menu()
