import tkinter as tk
from pages.homework import Homework
from pages.displayGrades import NoteDisplayPage
from pages.moduleOne import ModuleOne
from pages.moduleTwo import ModuleTwo
from pages.moduleThree import ModuleThree

class MyApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('MyApp')
        self.geometry('1024x1080')

        navbar = tk.Frame(self, bg="#5B0888", width=250)
        navbar.pack(side="left", fill="y")

        self.pages = {
            "Module I": ModuleOne(self),
            "Module II": ModuleTwo(self),
            "Module III": ModuleThree(self),
            "Homework": Homework(self),
            "Catalog": NoteDisplayPage(self),
        }

        for name, page in self.pages.items():
            button = tk.Button(navbar, text=name, command=lambda page=page: self.show_page(page), 
                               bg="white", fg="black", bd=0, relief=tk.FLAT,
                               width=15, height=2, font=("Arial", 12), 
                               highlightbackground="#5B0888", highlightthickness=2, 
                               borderwidth=0, highlightcolor="#5B0888", padx=10, pady=5)
            button.pack(side="top", fill="x", padx=5, pady=5)

        self.show_page(self.pages["Module I"])

        
    def show_page(self, page):
        if hasattr(self, "current_page"):
            self.current_page.pack_forget()
    
        page.pack(fill="both", expand=True)
        self.current_page = page

if __name__ == "__main__":
    app = MyApp()
    app.mainloop()