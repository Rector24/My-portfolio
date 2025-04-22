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
        self.root.config(bg='#0B2E33')

        self.title_label = tk.Label(root, text="The Book Haven Library", font=("Arial", 20, "bold"), fg="white",
                                    bg="#0B2E33")
        self.title_label.pack(pady=10)

        # Add buttons for navigation
        self.book_button = tk.Button(root, text="Manage Books", command=self.open_book_management, bg="#4F7C82", fg="white", width=12, height=2, padx=30)
        self.book_button.pack(pady=20)

        self.member_button = tk.Button(root, text="Manage Members", command=self.open_member_management, bg="#4F7C82", fg="white", width=12, height=2, padx=30)
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
        self.window.geometry("400x400")
        self.window.config(bg='#4F7C82')

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
        tk.Button(window, text="Add Book", command=self.add_book, bg="#4F7C82", fg="white").grid(row=5, column=0)
        tk.Button(window, text="Update Book", command=self.update_book, bg="#4F7C82", fg="white").grid(row=5, column=1)
        tk.Button(window, text="Delete Book", command=self.delete_book, bg="#4F7C82", fg="white").grid(row=6, column=0)
        tk.Button(window, text="View Books", command=self.view_books, bg="#4F7C82", fg="white").grid(row=6, column=1)
        tk.Button(window, text="Search Books", command=self.search_books, bg="#4F7C82", fg="white").grid(row=5, column=2)

        # Sorting buttons
        tk.Button(window, text="Sort by Title", command=lambda: self.sort_books('title'), bg="#4F7C82", fg="white").grid(row=7, column=2)
        tk.Button(window, text="Sort by Author", command=lambda: self.sort_books('author'), bg="#4F7C82", fg="white").grid(row=8, column=2)
        tk.Button(window, text="Sort by Genre", command=lambda: self.sort_books('genre'), bg="#4F7C82", fg="white").grid(row=9, column=2)

        self.books_text = tk.Text(window, height=10, width=50)
        self.books_text.grid(row=10, column=0, columnspan=3)

    def add_book(self):
        title = self.title_entry.get()
        author = self.author_entry.get()
        isbn = self.isbn_entry.get()
        genre = self.genre_entry.get()
        availability = self.availability_entry.get()

        conn = None  # Initialize conn to None
        try:
            conn = connect_db()
            cursor = conn.cursor()
            cursor.execute('''INSERT INTO books (title, author, isbn, genre, availability) VALUES (?, ?, ?, ?, ?)''',
                           (title, author, isbn, genre, availability))
            conn.commit()
            print("Book added successfully!")
        except sqlite3.IntegrityError:
            print("Error: ISBN already exists.")
        except Exception as e:
            print(f"An error occurred: {e}")
        finally:
            if conn is not None:
                conn.close()

    def update_book(self):
        isbn = self.isbn_entry.get()
        title = self.title_entry.get()
        author = self.author_entry.get()
        genre = self.genre_entry.get()
        availability = self.availability_entry.get()

        conn = None  # Initialize conn to None
        try:
            conn = connect_db()
            cursor = conn.cursor()
            cursor.execute('''UPDATE books SET title=?, author=?, genre=?, availability=? WHERE isbn=?''',
                           (title, author, genre, availability, isbn))
            if cursor.rowcount == 0:
                print("Error: Book not found.")
            else:
                conn.commit()
                print("Book updated successfully!")
        except Exception as e:
            print(f"An error occurred: {e}")
        finally:
            if conn is not None:
                conn.close()

    def delete_book(self):
        isbn = self.isbn_entry.get()

        conn = None  # Initialize conn to None
        try:
            conn = connect_db()
            cursor = conn.cursor()
            cursor.execute('''DELETE FROM books WHERE isbn=?''', (isbn,))
            if cursor.rowcount == 0:
                print("Error: Book not found.")
            else:
                conn.commit()
                print("Book deleted successfully!")
        except Exception as e:
            print(f"An error occurred: {e}")
        finally:
            if conn is not None:
                conn.close()

    def view_books(self):
        conn = connect_db()
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM books')
        rows = cursor.fetchall()
        conn.close()

        self.books_text.delete(1.0, tk.END)
        if not rows:
            self.books_text.insert(tk.END, "No books available.")
        else:
            for row in rows:
                book_info = f"ID: {row[0]}, Title: {row[1]}, Author: {row[2]}, ISBN: {row[3]}, Genre: {row[4]}, Availability: {row[5]}\n"
                self.books_text.insert(tk.END, book_info + "\n")

    def search_books(self):
        search_term = self.title_entry.get()  # Using title entry for search input
        conn = None  # Initialize conn to None
        try:
            conn = connect_db()
            cursor = conn.cursor()
            cursor.execute('''SELECT * FROM books WHERE title LIKE ? OR author LIKE ? OR isbn LIKE ?''',
                           (f'%{search_term}%', f'%{search_term}%', f'%{search_term}%'))
            rows = cursor.fetchall()
            self.books_text.delete(1.0, tk.END)  # Clear previous results
            if not rows:
                self.books_text.insert(tk.END, "No matching books found.")
            else:
                for row in rows:
                    book_info = f"ID: {row[0]}, Title: {row[1]}, Author: {row[2]}, ISBN: {row[3]}, Genre: {row[4]}, Availability: {row[5]}\n"
                    self.books_text.insert(tk.END, book_info + "\n")
        except Exception as e:
            print(f"An error occurred: {e}")
        finally:
            if conn is not None:
                conn.close()

    def sort_books(self, sort_by):
        conn = None  # Initialize conn to None
        try:
            conn = connect_db()
            cursor = conn.cursor()
            cursor.execute(f'SELECT * FROM books ORDER BY {sort_by}')
            rows = cursor.fetchall()
            self.books_text.delete(1.0, tk.END)  # Clear previous results
            if not rows:
                self.books_text.insert(tk.END, "No books available.")
            else:
                for row in rows:
                    book_info = f"ID: {row[0]}, Title: {row[1]}, Author: {row[2]}, ISBN: {row[3]}, Genre: {row[4]}, Availability: {row[5]}\n"
                    self.books_text.insert(tk.END, book_info + "\n")
        except Exception as e:
            print(f"An error occurred: {e}")
        finally:
            if conn is not None:
                conn.close()

# Member Management Window
class MemberManagement:
    def __init__(self, window):
        self.window = window
        self.window.geometry("400x400")
        self.window.config(bg='#4F7C82')

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
        tk.Button(window, text="Add Member", command=self.add_member, bg="#4F7C82", fg="white").grid(row=4, column=0)
        tk.Button(window, text="Update Member", command=self.update_member, bg="#4F7C82", fg="white").grid(row=4, column=1)
        tk.Button(window, text="Delete Member", command=self.delete_member, bg="#4F7C82", fg="white").grid(row=5, column=0)
        tk.Button(window, text="View Members", command=self.view_members, bg="#4F7C82", fg="white").grid(row=5, column=1)
        tk.Button(window, text="Search Members", command=self.search_members, bg="#4F7C82", fg="white").grid(row=4, column=2)

        # Sorting buttons
        tk.Button(window, text="Sort by Name", command=lambda: self.sort_members('name'), bg="#4F7C82", fg="white").grid(row=6, column=2)
        tk.Button(window, text="Sort by Member ID", command=lambda: self.sort_members('member_id'), bg="#4F7C82", fg="white").grid(row=7, column=2)

        self.members_text = tk.Text(window, height=10, width=50)
        self.members_text.grid(row=7, column=0, columnspan=2)

    def add_member(self):
        name = self.name_entry.get()
        member_id = self.member_id_entry.get()
        contact = self.contact_entry.get()
        membership_type = self.type_entry.get()

        conn = None  # Initialize conn to None
        try:
            conn = connect_db()
            cursor = conn.cursor()
            cursor.execute('''INSERT INTO members (name, member_id, contact, membership_type) VALUES (?, ?, ?, ?)''',
                           (name, member_id, contact, membership_type))
            conn.commit()
            print("Member added successfully!")
        except sqlite3.IntegrityError:
            print("Error: Membership ID already exists.")
        except Exception as e:
            print(f"An error occurred: {e}")
        finally:
            if conn is not None:
                conn.close()

    def update_member(self):
        member_id = self.member_id_entry.get()
        name = self.name_entry.get()
        contact = self.contact_entry.get()
        membership_type = self.type_entry.get()

        conn = None  # Initialize conn to None
        try:
            conn = connect_db()
            cursor = conn.cursor()
            cursor.execute('''UPDATE members SET name=?, contact=?, membership_type=? WHERE member_id=?''',
                           (name, contact, membership_type, member_id))
            if cursor.rowcount == 0:
                print("Error: Member not found.")
            else:
                conn.commit()
                print("Member updated successfully!")
        except Exception as e:
            print(f"An error occurred: {e}")
        finally:
            if conn is not None:
                conn.close()

    def delete_member(self):
        member_id = self.member_id_entry.get()

        conn = None  # Initialize conn to None
        try:
            conn = connect_db()
            cursor = conn.cursor()
            cursor.execute('''DELETE FROM members WHERE member_id=?''', (member_id,))
            if cursor.rowcount == 0:
                print("Error: Member not found.")
            else:
                conn.commit()
                print("Member deleted successfully!")
        except Exception as e:
            print(f"An error occurred: {e}")
        finally:
            if conn is not None:
                conn.close()

    def view_members(self):
        conn = connect_db()
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM members')
        rows = cursor.fetchall()
        conn.close()

        # Clear the text area before inserting new data
        self.members_text.delete("1.0", tk.END)

        # Insert member details into the text widget
        for row in rows:
            self.members_text.insert(tk.END,
                                      f"ID: {row[1]}, Name: {row[0]}, Member ID: {row[2]}, Contact: {row[3]}, Membership Type: {row[4]}\n")

    def search_members(self):
        search_term = self.name_entry.get()  # Using name entry for search input
        conn = None  # Initialize conn to None
        try:
            conn = connect_db()
            cursor = conn.cursor()
            cursor.execute('''SELECT * FROM members WHERE name LIKE ? OR member_id LIKE ?''',
                           (f'%{search_term}%', f'%{search_term}%'))
            rows = cursor.fetchall()
            self.members_text.delete(1.0, tk.END)  # Clear previous results
            if not rows:
                self.members_text.insert(tk.END, "No matching members found.")
            else:
                for row in rows:
                    self.members_text.insert(tk.END,
                                             f"ID: {row[1]}, Name: {row[0]}, Member ID: {row[2]}, Contact: {row[3]}, Membership Type: {row[4]}\n")
        except Exception as e:
            print(f"An error occurred: {e}")
        finally:
            if conn is not None:
                conn.close()

    def sort_members(self, sort_by):
        conn = None  # Initialize conn to None
        try:
            conn = connect_db()
            cursor = conn.cursor()
            cursor.execute(f'SELECT * FROM members ORDER BY {sort_by}')
            rows = cursor.fetchall()
            self.members_text.delete(1.0, tk.END)  # Clear previous results
            if not rows:
                self.members_text.insert(tk.END, "No members available.")
            else:
                for row in rows:
                    self.members_text.insert(tk.END,
                                             f"ID: {row[1]}, Name: {row[0]}, Member ID: {row[2]}, Contact: {row[3]}, Membership Type: {row[4]}\n")
        except Exception as e:
            print(f"An error occurred: {e}")
        finally:
            if conn is not None:
                conn.close()

# Create the database tables
create_tables()

# Run the application
if __name__ == "__main__":
    root = tk.Tk()
    app = LibraryApp(root)
    root.mainloop()