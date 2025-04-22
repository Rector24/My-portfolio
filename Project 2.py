import tkinter as tk
import sqlite3

# Connect to SQLite database (or create it if it doesn't exist)
def connect_db():
    return sqlite3.connect("library.db")

# Create tables for books and members
def create_tables():
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS books (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            author TEXT NOT NULL,
            isbn TEXT UNIQUE NOT NULL,
            genre TEXT,
            availability TEXT
        )
    ''')
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS members (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            member_id TEXT UNIQUE NOT NULL,
            contact TEXT,
            membership_type TEXT
        )
    ''')
    conn.commit()
    conn.close()

# Main Application Window
class LibraryApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Library Book and Member Management System")
        self.root.geometry("600x400")

        # Add buttons for navigation
        self.book_button = tk.Button(root, text="Manage Books", command=self.open_book_management)
        self.book_button.pack(pady=20)

        self.member_button = tk.Button(root, text="Manage Members", command=self.open_member_management)
        self.member_button.pack(pady=20)

    def open_book_management(self):
        # Open the book management window
        book_window = tk.Toplevel(self.root)
        book_window.title("Book Management")
        BookManagement(book_window)

    def open_member_management(self):
        # Open the member management window
        member_window = tk.Toplevel(self.root)
        member_window.title("Member Management")
        MemberManagement(member_window)

# Book Management Window
class BookManagement:
    def __init__(self, window):
        self.window = window
        self.window.geometry("400x300")

        # Input fields for books
        tk.Label(window, text="Book Title").grid(row=0, column=0)
        self.title_entry = tk.Entry(window)
        self.title_entry.grid(row=0, column=1)

        tk.Label(window, text="Author").grid(row=1, column=0)
        self.author_entry = tk.Entry(window)
        self.author_entry.grid(row=1, column=1)

        tk.Label(window, text="ISBN").grid(row=2, column=0)
        self.isbn_entry = tk.Entry(window)
        self.isbn_entry.grid(row=2, column=1)

        tk.Label(window, text="Genre").grid(row=3, column=0)
        self.genre_entry = tk.Entry(window)
        self.genre_entry.grid(row=3, column=1)

        tk.Label(window, text="Availability Status").grid(row=4, column=0)
        self.availability_entry = tk.Entry(window)
        self.availability_entry.grid(row=4, column=1)

        # Buttons for CRUD operations
        tk.Button(window, text="Add Book", command=self.add_book).grid(row=5, column=0)
        tk.Button(window, text="Update Book", command=self.update_book).grid(row=5, column=1)
        tk.Button(window, text="Delete Book", command=self.delete_book).grid(row=6, column=0)
        tk.Button(window, text="View Books", command=self.view_books).grid(row=6, column=1)

    def add_book(self):
        title = self.title_entry.get()
        author = self.author_entry.get()
        isbn = self.isbn_entry.get()
        genre = self.genre_entry.get()
        availability = self.availability_entry.get()

        conn = connect_db()
        cursor = conn.cursor()
        cursor.execute('''
            INSERT INTO books (title, author, isbn, genre, availability)
            VALUES (?, ?, ?, ?, ?)
        ''', (title, author, isbn, genre, availability))
        conn.commit()
        conn.close()
        print("Book added successfully!")

    def update_book(self):
        isbn = self.isbn_entry.get()
        title = self.title_entry.get()
        author = self.author_entry.get()
        genre = self.genre_entry.get()
        availability = self.availability_entry.get()

        conn = connect_db()
        cursor = conn.cursor()
        cursor.execute('''
            UPDATE books
            SET title=?, author=?, genre=?, availability=?
            WHERE isbn=?
        ''', (title, author, genre, availability, isbn))
        conn.commit()
        conn.close()
        print("Book updated successfully!")

    def delete_book(self):
        isbn = self.isbn_entry.get()

        conn = connect_db()
        cursor = conn.cursor()
        cursor.execute('''
            DELETE FROM books
            WHERE isbn=?
        ''', (isbn,))
        conn.commit()
        conn.close()
        print("Book deleted successfully!")

    def view_books(self):
        conn = connect_db()
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM books')
        rows = cursor.fetchall()
        conn.close()

        for row in rows:
            print(row)

# Member Management Window
class MemberManagement:
    def __init__(self, window):
        self.window = window
        self.window.geometry("400x300")

        # Input fields for members
        tk.Label(window, text="Member Name").grid(row=0, column=0)
        self.name_entry = tk.Entry(window)
        self.name_entry.grid(row=0, column=1)

        tk.Label(window, text="Membership ID").grid(row=1, column=0)
        self.member_id_entry = tk.Entry(window)
        self.member_id_entry.grid(row=1, column=1)

        tk.Label(window, text="Contact Information").grid(row=2, column=0)
        self.contact_entry = tk.Entry(window)
        self.contact_entry.grid(row=2, column=1)

        tk.Label(window, text="Membership Type").grid(row=3, column=0)
        self.type_entry = tk.Entry(window)
        self.type_entry.grid(row=3, column=1)

        # Buttons for CRUD operations
        tk.Button(window, text="Add Member", command=self.add_member).grid(row=4, column=0)
        tk.Button(window, text="Update Member", command=self.update_member).grid(row=4, column=1)
        tk.Button(window, text="Delete Member", command=self.delete_member).grid(row=5, column=0)
        tk.Button(window, text="View Members", command=self.view_members).grid(row=5, column=1)

    def add_member(self):
        name = self.name_entry.get()
        member_id = self.member_id_entry.get()
        contact = self.contact_entry.get()
        membership_type = self.type_entry.get()

        conn = connect_db()
        cursor = conn.cursor()
        cursor.execute('''
            INSERT INTO members (name, member_id, contact, membership_type)
            VALUES (?, ?, ?, ?)
        ''', (name, member_id, contact, membership_type))
        conn.commit()
        conn.close()
        print("Member added successfully!")

    def update_member(self):
        member_id = self.member_id_entry.get()
        name = self.name_entry.get()
        contact = self.contact_entry.get()
        membership_type = self.type_entry.get()

        conn = connect_db()
        cursor = conn.cursor()
        cursor.execute('''
            UPDATE members
            SET name=?, contact=?, membership_type=?
            WHERE member_id=?
        ''', (name, contact, membership_type, member_id))
        conn.commit()
        conn.close()
        print("Member updated successfully!")

    def delete_member(self):
        member_id = self.member_id_entry.get()

        conn = connect_db()
        cursor = conn.cursor()
        cursor.execute('''
            DELETE FROM members
            WHERE member_id=?
        ''', (member_id,))
        conn.commit()
        conn.close()
        print("Member deleted successfully!")

    def view_members(self):
        conn = connect_db()
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM members')
        rows = cursor.fetchall()
        conn.close()

        for row in rows:
            print(row)

# Run the application
if __name__ == "__main__":
    create_tables()  # Ensure tables are created before running the app
    root = tk.Tk()
    app = LibraryApp(root)
    root.mainloop()

#milestone 2
#question 1
import sqlite3

def connect_db():
    return sqlite3.connect("library.db")

def create_tables():
    conn = connect_db()
    cursor = conn.cursor()

    # Books
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS books (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            author TEXT NOT NULL,
            isbn TEXT UNIQUE NOT NULL,
            genre TEXT,
            availability TEXT DEFAULT 'Available'
        )
    ''')

    # Members
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS members (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            member_id TEXT UNIQUE NOT NULL,
            contact TEXT,
            membership_type TEXT
        )
    ''')

    # Borrowedbooks
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS borrowed_books (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            book_id INTEGER,
            member_id INTEGER,
            borrow_date TEXT,
            return_date TEXT,
            FOREIGN KEY (book_id) REFERENCES books(id) ON DELETE CASCADE,
            FOREIGN KEY (member_id) REFERENCES members(id) ON DELETE CASCADE
        )
    ''')

    conn.commit()
    conn.close()

if __name__ == "__main__":
    create_tables()
    print("Tables created successfully.")

#question 2
from tkinter import ttk, messagebox


# Connecting to the SQLite database
def connect_db():
    return sqlite3.connect("library.db")

def create_tables():
    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS books (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            author TEXT NOT NULL,
            isbn TEXT UNIQUE NOT NULL,
            genre TEXT,
            availability TEXT DEFAULT 'Available'
        )
    ''')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS members (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            member_id TEXT UNIQUE NOT NULL,
            contact TEXT,
            membership_type TEXT
        )
    ''')

    conn.commit()
    conn.close()


class LibraryApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Library Management System")
        self.root.geometry("600x400")

        tk.Label(root, text="Library Management System", font=("Arial", 16)).pack(pady=10)

        tk.Button(root, text="Manage Books", command=self.open_book_management, width=20).pack(pady=10)
        tk.Button(root, text="Manage Members", command=self.open_member_management, width=20).pack(pady=10)

    def open_book_management(self):
        book_window = tk.Toplevel(self.root)
        book_window.title("Book Management")
        BookManagement(book_window)

    def open_member_management(self):
        member_window = tk.Toplevel(self.root)
        member_window.title("Member Management")
        MemberManagement(member_window)


class BookManagement:
    def __init__(self, window):
        self.window = window
        self.window.geometry("600x400")

        # Form Fields
        tk.Label(window, text="Title").grid(row=0, column=0)
        self.title_entry = tk.Entry(window)
        self.title_entry.grid(row=0, column=1)

        tk.Label(window, text="Author").grid(row=1, column=0)
        self.author_entry = tk.Entry(window)
        self.author_entry.grid(row=1, column=1)

        tk.Label(window, text="ISBN").grid(row=2, column=0)
        self.isbn_entry = tk.Entry(window)
        self.isbn_entry.grid(row=2, column=1)

        tk.Label(window, text="Genre").grid(row=3, column=0)
        self.genre_entry = tk.Entry(window)
        self.genre_entry.grid(row=3, column=1)

        tk.Label(window, text="Availability").grid(row=4, column=0)
        self.availability_entry = tk.Entry(window)
        self.availability_entry.grid(row=4, column=1)


        tk.Button(window, text="Add", command=self.add_book).grid(row=5, column=0)
        tk.Button(window, text="Update", command=self.update_book).grid(row=5, column=1)
        tk.Button(window, text="Delete", command=self.delete_book).grid(row=6, column=0)
        tk.Button(window, text="View", command=self.view_books).grid(row=6, column=1)


        self.tree = ttk.Treeview(window, columns=("ID", "Title", "Author", "ISBN", "Genre", "Availability"), show="headings")
        self.tree.grid(row=7, column=0, columnspan=2, pady=10)
        for col in self.tree["columns"]:
            self.tree.heading(col, text=col)


    def add_book(self):
        title = self.title_entry.get()
        author = self.author_entry.get()
        isbn = self.isbn_entry.get()
        genre = self.genre_entry.get()
        availability = self.availability_entry.get()

        if not (title and author and isbn):
            messagebox.showwarning("Input Error", "Title, Author, and ISBN are required!")
            return

        conn = connect_db()
        cursor = conn.cursor()
        try:
            cursor.execute("INSERT INTO books (title, author, isbn, genre, availability) VALUES (?, ?, ?, ?, ?)",
                           (title, author, isbn, genre, availability))
            conn.commit()
            messagebox.showinfo("Success", "Book added successfully!")
            self.view_books()
        except sqlite3.IntegrityError:
            messagebox.showerror("Error", "ISBN must be unique!")
        finally:
            conn.close()

    def update_book(self):
        isbn = self.isbn_entry.get()
        title = self.title_entry.get()
        author = self.author_entry.get()
        genre = self.genre_entry.get()
        availability = self.availability_entry.get()

        if not isbn:
            messagebox.showwarning("Input Error", "ISBN is required to update a book!")
            return

        conn = connect_db()
        cursor = conn.cursor()
        cursor.execute("UPDATE books SET title=?, author=?, genre=?, availability=? WHERE isbn=?",
                       (title, author, genre, availability, isbn))
        conn.commit()
        conn.close()
        messagebox.showinfo("Success", "Book updated successfully!")
        self.view_books()

    def delete_book(self):
        isbn = self.isbn_entry.get()

        if not isbn:
            messagebox.showwarning("Input Error", "ISBN is required to delete a book!")
            return

        conn = connect_db()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM books WHERE isbn=?", (isbn,))
        conn.commit()
        conn.close()
        messagebox.showinfo("Success", "Book deleted successfully!")
        self.view_books()

    def view_books(self):
        conn = connect_db()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM books")
        rows = cursor.fetchall()
        conn.close()

        self.tree.delete(*self.tree.get_children())
        for row in rows:
            self.tree.insert("", tk.END, values=row)


class MemberManagement:
    def __init__(self, window):
        self.window = window
        self.window.geometry("600x400")

        tk.Label(window, text="Name").grid(row=0, column=0)
        self.name_entry = tk.Entry(window)
        self.name_entry.grid(row=0, column=1)

        tk.Label(window, text="Member ID").grid(row=1, column=0)
        self.member_id_entry = tk.Entry(window)
        self.member_id_entry.grid(row=1, column=1)

        tk.Button(window, text="Add Member", command=self.add_member).grid(row=2, column=0)
        tk.Button(window, text="View Members", command=self.view_members).grid(row=2, column=1)

    def add_member(self):
        name = self.name_entry.get()
        member_id = self.member_id_entry.get()

        conn = connect_db()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO members (name, member_id) VALUES (?, ?)", (name, member_id))
        conn.commit()
        conn.close()
        messagebox.showinfo("Success", "Member added successfully!")

    def view_members(self):
        pass  # Implement similar to books


if __name__ == "__main__":
    create_tables()
    root = tk.Tk()
    app = LibraryApp(root)
    root.mainloop()

