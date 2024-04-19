import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import sqlite3
import customtkinter as ctk

class addGrades(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.master = master
        self.create_widgets()

    def create_widgets(self):
        main_frame = ctk.CTkFrame(self, fg_color="#f0f0f0")
        main_frame.pack(fill="both", expand=False)

        content_frame = ctk.CTkFrame(main_frame, fg_color="#f0f0f0")
        content_frame.pack(side="left", fill="both", expand=True, padx=20, pady=20)

        self.tree = ttk.Treeview(content_frame, columns=("ID", "Name", "Grade", "Registration Grade Date", "Module"), show="headings")
        self.tree.heading("ID", text="ID")
        self.tree.heading("Name", text="User Name")
        self.tree.heading("Grade", text="Grade")
        self.tree.heading("Registration Grade Date", text="Grades Date")
        self.tree.heading("Module", text="Module")
        self.tree.pack(fill="both", expand=True, padx=10, pady=10)

        style = ttk.Style()
        style.configure('Treeview.Heading', font=('Poppins', 12))

        self.show_users()

        form_frame = ctk.CTkFrame(content_frame, fg_color="#f0f0f0")
        form_frame.pack(pady=20, side="left")

        self.name_label = ctk.CTkLabel(form_frame, text="User Name:", font=('Poppins', 16), text_color='#000')
        self.name_label.grid(row=0, column=0, padx=5, pady=5, sticky='w')
        self.name_entry = ctk.CTkEntry(form_frame, text_color='#000', fg_color="#fff", border_width=1, width=180)
        self.name_entry.grid(row=0, column=1, padx=5, pady=5)

        self.grade_label = ctk.CTkLabel(form_frame, text="Grade:", font=('Poppins', 16), text_color='#000')
        self.grade_label.grid(row=1, column=0, padx=5, pady=5, sticky='w')
        self.grade_entry = ctk.CTkEntry(form_frame, text_color='#000', fg_color="#fff", border_width=1, width=180)
        self.grade_entry.grid(row=1, column=1, padx=5, pady=5)

        self.grade_reg_date_label = ctk.CTkLabel(form_frame, text="Grades date:", font=('Poppins', 16), text_color='#000')
        self.grade_reg_date_label.grid(row=2, column=0, padx=5, pady=5, sticky='w')
        self.grade_reg_date_entry = ctk.CTkEntry(form_frame, text_color='#000', fg_color="#fff", border_width=1, width=180)
        self.grade_reg_date_entry.grid(row=2, column=1, padx=5, pady=5)

        self.module_label = ctk.CTkLabel(form_frame, text="Module:", font=('Poppins', 16), text_color='#000')
        self.module_label.grid(row=3, column=0, padx=5, pady=5, sticky='w')
        self.module_entry = ctk.CTkEntry(form_frame, text_color='#000', fg_color="#fff", border_width=1, width=180)
        self.module_entry.grid(row=3, column=1, padx=5, pady=5)

        self.add_button = ctk.CTkButton(form_frame, fg_color='#5B0888', text="Add Grades", text_color='#fff', font=("Poppins", 14), width=180, command=self.add_grade)
        self.add_button.grid(row=0, column=2, columnspan=2, padx=5, pady=5, sticky='w')

        self.remove_button = ctk.CTkButton(form_frame, text="Delete user", fg_color='#5B0888', text_color='#fff', font=("Poppins", 14), width=180, command=self.remove_grade)
        self.remove_button.grid(row=1, column=2, columnspan=2, padx=5, pady=5, sticky='w')

        self.clear_button = ctk.CTkButton(form_frame, text="Cleare Inputs", fg_color='#5B0888', text_color='#fff', font=("Poppins", 14), width=180, command=self.clear_entries)
        self.clear_button.grid(row=2, column=2, columnspan=2, padx=5, pady=5, sticky='w')

        self.sort_button = ctk.CTkButton(form_frame, text="Alphabetical Sort", fg_color='#5B0888', text_color='#fff', font=("Poppins", 14), width=180, command=self.sort_users)
        self.sort_button.grid(row=3, column=2, columnspan=2, padx=5, pady=5, sticky='w')

    

    def show_users(self):
        for i in self.tree.get_children():
            self.tree.delete(i)

        students = fetch_students()
        for student in students:
            self.tree.insert("", "end", values=student)

    def add_grade(self):
        name = self.name_entry.get()
        grade = self.grade_entry.get()
        grade_reg_date = self.grade_reg_date_entry.get()
        module = self.module_entry.get()

        if not name or not grade or not grade_reg_date or not module:
            messagebox.showerror("Error", "Please fill in all fields.")
            return

        insert_grade(name, grade, grade_reg_date, module)
        self.show_users()
        self.clear_entries()

    def remove_grade(self):
        selected_item = self.tree.selection()
        if not selected_item:
            messagebox.showerror("Error", "Please select a user to delete.")
            return

        user_id = self.tree.item(selected_item, 'values')[0]
        delete_user(user_id)
        self.show_users()

    def clear_entries(self):
        self.name_entry.delete(0, tk.END)
        self.grade_entry.delete(0, tk.END)
        self.grade_reg_date_entry.delete(0, tk.END)
        self.module_entry.delete(0, tk.END)

    def sort_users(self):
        sorted_users = sorted(fetch_students(), key=lambda x: x[1])
        for i in self.tree.get_children():
            self.tree.delete(i)
        for student in sorted_users:
            self.tree.insert("", "end", values=student)


def fetch_students():
    conn = sqlite3.connect('grades.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM grades')
    students = cursor.fetchall()
    conn.close()
    return students

def insert_grade(name, grade, grade_reg_date, module):
    conn = sqlite3.connect('grades.db')
    cursor = conn.cursor()
    cursor.execute('INSERT INTO grades (name, grade, grade_reg_date, module) VALUES (?, ?, ?, ?)', (name, grade, grade_reg_date, module))
    conn.commit()
    conn.close()

def delete_user(user_id):
    conn = sqlite3.connect('grades.db')
    cursor = conn.cursor()
    cursor.execute('DELETE FROM grades WHERE id = ?', (user_id,))
    conn.commit()
    conn.close()

def create_table():
    conn = sqlite3.connect('grades.db')
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS grades (
                        id INTEGER PRIMARY KEY,
                        name TEXT,
                        grade INTEGER,
                        grade_reg_date TEXT,
                        module TEXT)''')
    conn.commit()
    conn.close()   

create_table() 

if __name__ == "__main__":
    app = tk.Tk()
    page2 = addGrades(app)
    page2.pack(fill="both", expand=True)
    app.mainloop()