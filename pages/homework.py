import tkinter as tk
from tkinter import ttk, filedialog, messagebox
import sqlite3
import customtkinter as ctk

class Homework(tk.Frame):
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

        self.homework_tree = ttk.Treeview(content_frame, columns=("ID", "Title", "Description", "Date", "Image Path"), show="headings")
        self.homework_tree.heading("ID", text="ID")
        self.homework_tree.heading("Title", text="Title")
        self.homework_tree.heading("Description", text="Description")
        self.homework_tree.heading("Date", text="Date")
        self.homework_tree.heading("Image Path", text="Image")
        self.homework_tree.pack(fill="both", expand=True, padx=10, pady=10)
        self.homework_tree.bind("<ButtonRelease-1>", self.select_homework)

        form_frame = ctk.CTkFrame(content_frame, fg_color="#f0f0f0")
        form_frame.pack(pady=20, side="left")

        self.title_label = ctk.CTkLabel(form_frame, text="Title:", font=('Poppins', 14), text_color='#000', fg_color="#f0f0f0")
        self.title_label.grid(row=0, column=0, padx=5, pady=5, sticky='w')
        self.title_entry = ctk.CTkEntry(form_frame, text_color='#000', fg_color="#fff", border_width=1, width=180)
        self.title_entry.grid(row=0, column=1, padx=5, pady=5)

        self.description_label = ctk.CTkLabel(form_frame, text="Description:", font=('Poppins', 14), text_color='#000', fg_color="#f0f0f0")
        self.description_label.grid(row=1, column=0, padx=5, pady=5, sticky='w')
        self.description_entry = ctk.CTkTextbox(form_frame, text_color='#000', fg_color="#fff", border_width=1, width=180, height=10)
        self.description_entry.grid(row=1, column=1, padx=5, pady=5)

        self.deadline_label = ctk.CTkLabel(form_frame, text="Date:", font=('Poppins', 14), text_color='#000', fg_color="#f0f0f0")
        self.deadline_label.grid(row=2, column=0, padx=5, pady=5, sticky='w')
        self.deadline_entry = ctk.CTkEntry(form_frame, text_color='#000', fg_color="#fff", border_width=1, width=180)
        self.deadline_entry.grid(row=2, column=1, padx=5, pady=5)

        self.upload_image_button = ctk.CTkButton(form_frame, text="Uppload Image", fg_color='#5B0888', text_color='#fff', font=("Poppins", 14), width=180, command=self.upload_image)
        self.upload_image_button.grid(row=3, column=0, columnspan=2, padx=5, pady=5, sticky='w')

        self.image_label = ctk.CTkLabel(form_frame, text="", font=('Poppins', 12), text_color='#000', fg_color="#f0f0f0")
        self.image_label.grid(row=3, column=2, columnspan=2, padx=5, pady=5, sticky='w')

        self.add_homework_button = ctk.CTkButton(form_frame, text="Add Homework", fg_color='#5B0888', text_color='#fff', font=("Poppins", 14), width=180, command=self.add_homework)
        self.add_homework_button.grid(row=4, column=0, columnspan=2, padx=5, pady=5, sticky='w')

        self.edit_button = ctk.CTkButton(form_frame, text="Edit Homework", fg_color='#5B0888', text_color='#fff', font=("Poppins", 14), width=180, command=self.edit_homework)
        self.edit_button.grid(row=5, column=0, columnspan=2, padx=5, pady=5, sticky='w')

        self.delete_button = ctk.CTkButton(form_frame, text="Delete homework", fg_color='#5B0888', text_color='#fff', font=("Poppins", 14), width=180, command=self.delete_homework)
        self.delete_button.grid(row=6, column=0, columnspan=2, padx=5, pady=5, sticky='w')

        self.clear_button = ctk.CTkButton(form_frame, text="Cleare Inputs", fg_color='#5B0888', text_color='#fff', font=("Poppins", 14), width=180, command=self.clear_entries)
        self.clear_button.grid(row=7, column=0, columnspan=2, padx=5, pady=5, sticky='w')

    def load_homeworks(self):
        self.homework_tree.delete(*self.homework_tree.get_children())

        conn = sqlite3.connect('homework.db')
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM homework')
        for row in cursor.fetchall():
            self.homework_tree.insert("", "end", values=row)
        conn.close()

    def upload_image(self):
        filename = filedialog.askopenfilename(title="Select image", filetypes=[("Images", "*.jpg;*.jpeg;*.png;*.gif")])
        if filename:
            self.image_label.configure(text=filename)

    def add_homework(self):
        title = self.title_entry.get()
        description = self.description_entry.get("1.0", tk.END)
        deadline = self.deadline_entry.get()
        image_path = self.image_label.cget("text")

        if not title or not description.strip() or not deadline:
            messagebox.showerror("Eroare", "Please fill all fields!")
            return

        conn = sqlite3.connect('homework.db')
        cursor = conn.cursor()
        cursor.execute('INSERT INTO homework (title, description, deadline, image_path) VALUES (?, ?, ?, ?)', (title, description, deadline, image_path))
        conn.commit()
        conn.close()

        messagebox.showinfo("Succes", "Homework added successfully!")
        self.load_homeworks()

    def select_homework(self, event):
        item = self.homework_tree.selection()[0]
        values = self.homework_tree.item(item, "values")
        self.title_entry.delete(0, tk.END)
        self.title_entry.insert(0, values[1])
        self.description_entry.delete("1.0", tk.END)
        self.description_entry.insert(tk.END, values[2])
        self.deadline_entry.delete(0, tk.END)
        self.deadline_entry.insert(0, values[3])
        self.image_label.configure(text=values[4])

    def edit_homework(self):
        item = self.homework_tree.selection()[0]
        homework_id = self.homework_tree.item(item, "values")[0]
        title = self.title_entry.get()
        description = self.description_entry.get("1.0", tk.END)
        deadline = self.deadline_entry.get()
        image_path = self.image_label.cget("text")

        if not title or not description.strip() or not deadline:
            messagebox.showerror("Eroare", "Please fill all fields!")
            return

        conn = sqlite3.connect('homework.db')
        cursor = conn.cursor()
        cursor.execute('UPDATE homework SET title=?, description=?, deadline=?, image_path=? WHERE id=?', (title, description, deadline, image_path, homework_id))
        conn.commit()
        conn.close()

        messagebox.showinfo("Succes", "Homework updated!")
        self.load_homeworks()

    def delete_homework(self):
        item = self.homework_tree.selection()[0]
        homework_id = self.homework_tree.item(item, "values")[0]

        conn = sqlite3.connect('homework.db')
        cursor = conn.cursor()
        cursor.execute('DELETE FROM homework WHERE id=?', (homework_id,))
        conn.commit()
        conn.close()

        messagebox.showinfo("Succes", "Homework deleted!")
        self.load_homeworks()

    def clear_entries(self):
        self.title_entry.delete(0, tk.END)
        self.description_entry.delete("1.0", tk.END)
        self.deadline_entry.delete(0, tk.END)
        self.image_label.configure(text="")


def create_homework_table():
    conn = sqlite3.connect('homework.db')
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS homework (
                        id INTEGER PRIMARY KEY,
                        title TEXT,
                        description TEXT,
                        deadline TEXT,
                        image_path TEXT)''')
    conn.commit()
    conn.close()

def add_image_path_column():
    conn = sqlite3.connect('homework.db')
    cursor = conn.cursor()
    try:
        cursor.execute("ALTER TABLE homework ADD COLUMN image_path TEXT")
    except sqlite3.OperationalError as e:
        print("Error:", e)
    conn.commit()
    conn.close()

create_homework_table()
add_image_path_column()

if __name__ == "__main__":
    app = tk.Tk()
    page3 = Homework(app)
    page3.pack(fill="both", expand=True)
    app.mainloop()
