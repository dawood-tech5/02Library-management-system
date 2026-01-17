books = []

def add_book():
    book_id = input("Enter Book id: ")
    title = input("Enter Book Title: ")
    author = input("Enter Author Name: ")
    
    book = {
        "id": book_id,
        "title": title,
        "author": author,
        "available": True
    }
    
    books.append(book)
    print("Book added successfully")

def view_books():
    if not books:
        print("No books available")
    else:
        for b in books:
            print(b)

while True:
    print("\nLibrary Management System")
    print("1. Add Book")
    print("2. Display Books")
    print("3. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_book()
    elif choice == "2":
        view_books()
    elif choice == "3":
        print("Goodbye!")
        break
    else:
        print("Invalid choice")
