import tkinter as tk
from tkinter import ttk
import sqlite3

class NoteDisplayPage(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.master = master
        self.create_widgets()
        self.show_grades()  
        self.schedule_update()  

    def create_widgets(self):
        main_frame = tk.Frame(self)
        main_frame.pack(fill="both", expand=True)

        self.tree = ttk.Treeview(main_frame, columns=("ID", "Name", "Grade", "Registration Grade Date", "Module"), show="headings")
        self.tree.heading("ID", text="ID")
        self.tree.heading("Name", text="User Name")
        self.tree.heading("Grade", text="Grade")
        self.tree.heading("Registration Grade Date", text="Grades date")
        self.tree.heading("Module", text="Module")
        self.tree.pack(fill="both", expand=True, padx=10, pady=10)

    def show_grades(self):
        for i in self.tree.get_children():
            self.tree.delete(i)

        grades = fetch_grades_from_db()
        for grade in grades:
            self.tree.insert("", "end", values=grade)

    def schedule_update(self):
        self.show_grades() 
        self.after(5000, self.schedule_update)  

def fetch_grades_from_db():
    conn = sqlite3.connect('grades.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM grades')
    grades = cursor.fetchall()
    conn.close()
    return grades

if __name__ == "__main__":
    app = tk.Tk()
    note_display_page = NoteDisplayPage(app)
    note_display_page.pack(fill="both", expand=True)
    app.mainloop()
