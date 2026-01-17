# FIRST WE USE LIST
books = []

# THEN FUNCTION
def add_book():
    book_id = input("Enter Book id: ")
    title = input("Enter Book Title: ")
    author = input("Enter Author Name: ")
    
    # NOW WE USE DICTIONARY
    book = {
        "id": book_id,
        "title": title,
        "author": author,
        "available": True
    }
    
    books.append(book)  # APPEND DICTIONARY TO LIST
    print("Book added successfully ✅")

def view_books():
    if not books:
        print("No books available ❌")
    else:
        for book in books:
            print(book)

# NOW WE USE LOOP
while True:
    print("\n📘 Library Management System")
    print("1. Add Book")
    print("2. Display Books")
    print("3. Exit")

    choice = input("Enter your choice: ")

    # CONDITIONAL STATEMENTS
    if choice == "1":
        add_book()
    elif choice == "2":
        view_books()
    elif choice == "3":
        print("Goodbye 👋")
        break
    else:
        print("Invalid choice ❌")
