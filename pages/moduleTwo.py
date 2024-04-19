import tkinter as tk

class ModuleTwo(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.master = master
        
        self.canvas = tk.Canvas(self, bg="white")
        self.scrollbar = tk.Scrollbar(self, orient="vertical", command=self.canvas.yview)
        self.scrollable_frame = tk.Frame(self.canvas)

        self.scrollable_frame.bind(
            "<Configure>",
            lambda e: self.canvas.configure(
                scrollregion=self.canvas.bbox("all")
            )
        )

        self.canvas.create_window((0, 0), window=self.scrollable_frame, anchor="nw")
        self.canvas.configure(yscrollcommand=self.scrollbar.set)

        self.add_content()

        self.canvas.pack(side="left", fill="both", expand=True)
        self.scrollbar.pack(side="right", fill="y")

    def add_content(self):
        self.label = tk.Label(self.scrollable_frame, text="Module 2", font=("Helvetica", 18))
        self.label.pack(pady=20)

        self.content_titlu_unu = tk.Label(self.scrollable_frame, text="Text 2.1 – Text", justify="left", wraplength=1310, font=(16))
        self.content_titlu_unu.pack(anchor="w", padx=20, pady=10)

        self.content_label = tk.Label(self.scrollable_frame, text="1.  Lorem ipsum, dolor sit amet consectetur adipisicing elit. Impedit quisquam enim eaque libero ut, at quibusdam excepturi praesentium tempore! Consectetur placeat facilis exercitationem eius unde molestias sit maiores odit asperiores voluptatum? Dolore delectus praesentium dolores id quibusdam blanditiis, nostrum veniam nisi, reiciendis repudiandae voluptate explicabo natus perferendis repellat ullam labore.", justify="left", wraplength=1310)
        self.content_label.pack(anchor="w", padx=20, pady=10)

        self.label2 = tk.Label(self.scrollable_frame, text="2. Lorem ipsum, dolor sit amet consectetur adipisicing elit. Impedit quisquam enim eaque libero ut, at quibusdam excepturi praesentium tempore! Consectetur placeat facilis exercitationem eius unde molestias sit maiores odit asperiores voluptatum? Dolore delectus praesentium dolores id quibusdam blanditiis, nostrum veniam nisi, reiciendis repudiandae voluptate explicabo natus perferendis repellat ullam labore.", justify="left", wraplength=1310)
        self.label2.pack(anchor="w", padx=20, pady=10)

        self.label3 = tk.Label(self.scrollable_frame, text="3. Lorem ipsum, dolor sit amet consectetur adipisicing elit. Impedit quisquam enim eaque libero ut, at quibusdam excepturi praesentium tempore! Consectetur placeat facilis exercitationem eius unde molestias sit maiores odit asperiores voluptatum? Dolore delectus praesentium dolores id quibusdam blanditiis, nostrum veniam nisi, reiciendis repudiandae voluptate explicabo natus perferendis repellat ullam labore. ", justify="left", wraplength=1310)
        self.label3.pack(anchor="w", padx=20, pady=10)

        self.label4 = tk.Label(self.scrollable_frame, text="4. Lorem ipsum, dolor sit amet consectetur adipisicing elit. Impedit quisquam enim eaque libero ut, at quibusdam excepturi praesentium tempore! Consectetur placeat facilis exercitationem eius unde molestias sit maiores odit asperiores voluptatum? Dolore delectus praesentium dolores id quibusdam blanditiis, nostrum veniam nisi, reiciendis repudiandae voluptate explicabo natus perferendis repellat ullam labore.", justify="left", wraplength=1310)
        self.label4.pack(anchor="w", padx=20, pady=10)

        self.label5 = tk.Label(self.scrollable_frame, text="Text 2.2 – Text", justify="left", wraplength=1310, font=(16))
        self.label5.pack(anchor="w", padx=20, pady=10)

        self.label6 = tk.Label(self.scrollable_frame, text="Lorem ipsum, dolor sit amet consectetur adipisicing elit. Impedit quisquam enim eaque libero ut, at quibusdam excepturi praesentium tempore! Consectetur placeat facilis exercitationem eius unde molestias sit maiores odit asperiores voluptatum? Dolore delectus praesentium dolores id quibusdam blanditiis, nostrum veniam nisi, reiciendis repudiandae voluptate explicabo natus perferendis repellat ullam labore.", justify="left", wraplength=1310)
        self.label6.pack(anchor="w", padx=20, pady=10)

        self.label7 = tk.Label(self.scrollable_frame, text="a. Lorem ipsum, dolor sit amet consectetur adipisicing elit. Impedit quisquam enim eaque libero ut, at quibusdam excepturi praesentium tempore! Consectetur placeat facilis exercitationem eius unde molestias sit maiores odit asperiores voluptatum? Dolore delectus praesentium dolores id quibusdam blanditiis, nostrum veniam nisi, reiciendis repudiandae voluptate explicabo natus perferendis repellat ullam labore.", justify="left", wraplength=1310)
        self.label7.pack(anchor="w", padx=20, pady=10)

        self.label8 = tk.Label(self.scrollable_frame, text="b. Lorem ipsum, dolor sit amet consectetur adipisicing elit. Impedit quisquam enim eaque libero ut, at quibusdam excepturi praesentium tempore! Consectetur placeat facilis exercitationem eius unde molestias sit maiores odit asperiores voluptatum? Dolore delectus praesentium dolores id quibusdam blanditiis, nostrum veniam nisi, reiciendis repudiandae voluptate explicabo natus perferendis repellat ullam labore.", justify="left", wraplength=1310)
        self.label8.pack(anchor="w", padx=20, pady=10)


        self.label9 = tk.Label(self.scrollable_frame, text="2. Lorem ipsum, dolor sit amet consectetur adipisicing elit. Impedit quisquam enim eaque libero ut, at quibusdam excepturi praesentium tempore! Consectetur placeat facilis exercitationem eius unde molestias sit maiores odit asperiores voluptatum? Dolore delectus praesentium dolores id quibusdam blanditiis, nostrum veniam nisi, reiciendis repudiandae voluptate explicabo natus perferendis repellat ullam labore.", justify="left", wraplength=1310)
        self.label9.pack(anchor="w", padx=20, pady=10)

        self.label10 = tk.Label(self.scrollable_frame, text="Text 2.3 – Text", justify="left", wraplength=1310, font=(16))
        self.label10.pack(anchor="w", padx=20, pady=10)        

        self.label11 = tk.Label(self.scrollable_frame, text="1.	Lorem ipsum, dolor sit amet consectetur adipisicing elit. Impedit quisquam enim eaque libero ut, at quibusdam excepturi praesentium tempore! Consectetur placeat facilis exercitationem eius unde molestias sit maiores odit asperiores voluptatum? Dolore delectus praesentium dolores id quibusdam blanditiis, nostrum veniam nisi, reiciendis repudiandae voluptate explicabo natus perferendis repellat ullam labore.", justify="left", wraplength=1310)
        self.label11.pack(anchor="w", padx=20, pady=10)

        self.label12 = tk.Label(self.scrollable_frame, text="2.	Lorem ipsum, dolor sit amet consectetur adipisicing elit. Impedit quisquam enim eaque libero ut, at quibusdam excepturi praesentium tempore! Consectetur placeat facilis exercitationem eius unde molestias sit maiores odit asperiores voluptatum? Dolore delectus praesentium dolores id quibusdam blanditiis, nostrum veniam nisi, reiciendis repudiandae voluptate explicabo natus perferendis repellat ullam labore.", justify="left", wraplength=1310)
        self.label12.pack(anchor="w", padx=20, pady=10)

        self.label9 = tk.Label(self.scrollable_frame, text="3. Lorem ipsum, dolor sit amet consectetur adipisicing elit. Impedit quisquam enim eaque libero ut, at quibusdam excepturi praesentium tempore! Consectetur placeat facilis exercitationem eius unde molestias sit maiores odit asperiores voluptatum? Dolore delectus praesentium dolores id quibusdam blanditiis, nostrum veniam nisi, reiciendis repudiandae voluptate explicabo natus perferendis repellat ullam labore.", justify="left", wraplength=1310)
        self.label9.pack(anchor="w", padx=20, pady=10)
        
        self.label10 = tk.Label(self.scrollable_frame, text="b. Lorem ipsum, dolor sit amet consectetur adipisicing elit. Impedit quisquam enim eaque libero ut, at quibusdam excepturi praesentium tempore! Consectetur placeat facilis exercitationem eius unde molestias sit maiores odit asperiores voluptatum? Dolore delectus praesentium dolores id quibusdam blanditiis, nostrum veniam nisi, reiciendis repudiandae voluptate explicabo natus perferendis repellat ullam labore. ", justify="left", wraplength=1310)
        self.label10.pack(anchor="w", padx=20, pady=10)

        self.label11 = tk.Label(self.scrollable_frame, text="c. Lorem ipsum, dolor sit amet consectetur adipisicing elit. Impedit quisquam enim eaque libero ut, at quibusdam excepturi praesentium tempore! Consectetur placeat facilis exercitationem eius unde molestias sit maiores odit asperiores voluptatum? Dolore delectus praesentium dolores id quibusdam blanditiis, nostrum veniam nisi, reiciendis repudiandae voluptate explicabo natus perferendis repellat ullam labore.", justify="left", wraplength=1310)
        self.label11.pack(anchor="w", padx=20, pady=10)

        self.label12 = tk.Label(self.scrollable_frame, text="2.Lorem ipsum, dolor sit amet consectetur adipisicing elit. Impedit quisquam enim eaque libero ut, at quibusdam excepturi praesentium tempore! Consectetur placeat facilis exercitationem eius unde molestias sit maiores odit asperiores voluptatum? Dolore delectus praesentium dolores id quibusdam blanditiis, nostrum veniam nisi, reiciendis repudiandae voluptate explicabo natus perferendis repellat ullam labore.", justify="left", wraplength=1310)
        self.label12.pack(anchor="w", padx=20, pady=10)

        self.label13 = tk.Label(self.scrollable_frame, text="3.	Lorem ipsum, dolor sit amet consectetur adipisicing elit. Impedit quisquam enim eaque libero ut, at quibusdam excepturi praesentium tempore! Consectetur placeat facilis exercitationem eius unde molestias sit maiores odit asperiores voluptatum? Dolore delectus praesentium dolores id quibusdam blanditiis, nostrum veniam nisi, reiciendis repudiandae voluptate explicabo natus perferendis repellat ullam labore.", justify="left", wraplength=1310)
        self.label13.pack(anchor="w", padx=20, pady=10)


    def show(self):
        self.pack_forget()
        self.master.show_page(self)
