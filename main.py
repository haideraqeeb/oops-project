import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from tkinter import simpledialog

class Library:
    def __init__(self, listofBooks):
        self.books = listofBooks

    def displayAvailableBooks(self):
        return "\n".join(self.books)

    def borrowBook(self, name, bookname, track):
        if bookname not in self.books:
            return f"{bookname} BOOK IS NOT AVAILABLE EITHER TAKEN BY SOMEONE ELSE, WAIT UNTIL HE RETURNED."
        else:
            track.append({name: bookname})
            self.books.remove(bookname)
            return "BOOK ISSUED : THANK YOU KEEP IT WITH CARE AND RETURN ON TIME."

    def returnBook(self, bookname, track):
        for borrowerMap in track:
            if borrowerMap.values() == bookname:
                track.remove(borrowerMap)
                break
        self.books.append(bookname)
        return "BOOK RETURNED : THANK YOU!"

    def donateBook(self, bookname):
        self.books.append(bookname)
        return "BOOK DONATED : THANK YOU VERY MUCH, HAVE A GREAT DAY AHEAD."

class Student:
    def requestBook(self, bookname):
        return bookname

    def returnBook(self, name, bookname, track):
        if {name: bookname} in track:
            track.remove({name: bookname})
            return "BOOK RETURNED : THANK YOU!"
        else:
            return "BOOK RETURN FAILED: You haven't borrowed this book."

    def donateBook(self, bookname):
        return bookname


class LibraryUI:
    def __init__(self, master):
        self.master = master
        self.master.title("Library Management System")
        self.master.geometry("500x300")
        self.master.configure(bg="#f0f0f0")

        self.style = ttk.Style()
        self.style.configure('TRoundedButton.TButton', 
                             font=('Arial', 12), 
                             padding=5, 
                             background='#4CAF50', 
                             foreground='#ffffff',
                             relief='flat',
                             borderwidth=0,
                             bordercolor='#4CAF50',
                             focusthickness=0,
                             focuscolor='#4CAF50',
                             borderradius=20)
        self.style.map('TRoundedButton.TButton',
                       background=[('active', '#ffffff')],  # Change background color on hover
                       foreground=[('active', '#4CAF50')])  # Change text color on hover

        self.library = Library(["vistas", "invention", "rich&poor", "indian", "macroeconomics", "microeconomics"])
        self.student = Student()
        self.track = []

        self.label = ttk.Label(master, text="Library Management System", background='#f0f0f0')
        self.label.pack(pady=10)

        self.list_books_button = ttk.Button(master, text="List All Books", command=self.list_books, style='TRoundedButton.TButton')
        self.list_books_button.pack(pady=5, padx=20, fill='x')

        self.borrow_book_button = ttk.Button(master, text="Borrow Book", command=self.borrow_book_dialog, style='TRoundedButton.TButton')
        self.borrow_book_button.pack(pady=5, padx=20, fill='x')

        self.return_book_button = ttk.Button(master, text="Return Book", command=self.return_book_dialog, style='TRoundedButton.TButton')
        self.return_book_button.pack(pady=5, padx=20, fill='x')

        self.donate_book_button = ttk.Button(master, text="Donate Book", command=self.donate_book, style='TRoundedButton.TButton')
        self.donate_book_button.pack(pady=5, padx=20, fill='x')

    def list_books(self):
        available_books = self.library.displayAvailableBooks()
        messagebox.showinfo("Available Books", f"Available Books:\n{available_books}")

    def borrow_book_dialog(self):
        name = simpledialog.askstring("Borrow Book", "Enter your name:")
        if name:
            bookname = simpledialog.askstring("Borrow Book", "Enter name of the book you want to borrow:")
            if bookname:
                message = self.library.borrowBook(name, bookname, self.track)
                messagebox.showinfo("Borrow Book", message)

    def return_book_dialog(self):
        name = simpledialog.askstring("Return Book", "Enter your name:")
        if name:
            bookname = simpledialog.askstring("Return Book", "Enter name of the book you want to return:")
            if bookname:
                message = self.student.returnBook(name, bookname, self.track)
                messagebox.showinfo("Return Book", message)

    def donate_book(self):
        bookname = simpledialog.askstring("Donate Book", "Enter name of the book you want to donate:")
        if bookname:
            message = self.library.donateBook(bookname)
            messagebox.showinfo("Donate Book", message)

if __name__ == "__main__":
    root = tk.Tk()
    app = LibraryUI(root)
    root.mainloop()
