import tkinter as tk
from tkinter import ttk, filedialog, messagebox
import sqlite3
import customtkinter as ctk

class HomeworkListPage(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.master = master
        self.create_widgets()
        self.load_homeworks()

    def create_widgets(self):
        main_frame = ctk.CTkFrame(self, fg_color="#f0f0f0")
        main_frame.pack(fill="both", expand=False)

        content_frame = ctk.CTkFrame(main_frame, fg_color="#f0f0f0")
        content_frame.pack(side="left", fill="both", expand=True, padx=20, pady=20)

        self.homework_tree = ttk.Treeview(content_frame, columns=("ID", "Title", "Description", "Date"), show="headings")
        self.homework_tree.heading("ID", text="ID")
        self.homework_tree.heading("Title", text="Title")
        self.homework_tree.heading("Description", text="Description")
        self.homework_tree.heading("Date", text="Date")
        self.homework_tree.pack(fill="both", expand=True, padx=10, pady=10)

    def load_homeworks(self):
        self.homework_tree.delete(*self.homework_tree.get_children())

        conn = sqlite3.connect('homework.db')
        cursor = conn.cursor()
        cursor.execute('SELECT id, title, description, deadline FROM homework')
        for row in cursor.fetchall():
            self.homework_tree.insert("", "end", values=row)
        conn.close()


if __name__ == "__main__":
    app = tk.Tk()
    page3 = HomeworkListPage(app)
    page3.pack(fill="both", expand=True)
    app.mainloop()
