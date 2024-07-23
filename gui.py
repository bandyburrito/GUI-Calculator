import tkinter as tk

root = tk.Tk()

root.configure(bg="green")
root.geometry("500x500")
root.title("My first GUI App")




label = tk.Label(root, text="Welcome to our Calculator!", font=("Arial", 18))
label.pack(padx=20, pady=20)

textbox = tk.Text(root, height=3, font=("Arial", 16))
textbox.pack()

buttonframe = tk.Frame(root)
buttonframe.columnconfigure(0, weight=1)
buttonframe.columnconfigure(1, weight=1)
buttonframe.columnconfigure(2, weight=1)

#krijimi i butonave
but1 = tk.Button(buttonframe, text="1", font=("Arial", 16))
but1.grid(row=0, column=0, sticky=tk.W+tk.E)

buttonframe.pack(fill="x")


but2 = tk.Button(buttonframe, text="2", font=("Arial", 16))
but2.grid(row=0, column=1, sticky=tk.W+tk.E)

buttonframe.pack(fill="x")


but3 = tk.Button(buttonframe, text="3", font=("Arial", 16))
but3.grid(row=0, column=2, sticky=tk.W+tk.E)

buttonframe.pack(fill="x")


but4 = tk.Button(buttonframe, text="4", font=("Arial", 16))
but4.grid(row=1, column=0, sticky=tk.W+tk.E)

buttonframe.pack(fill="x")


but5 = tk.Button(buttonframe, text="5", font=("Arial", 16))
but5.grid(row=1, column=1, sticky=tk.W+tk.E)

buttonframe.pack(fill="x")


but6 = tk.Button(buttonframe, text="6", font=("Arial", 16))
but6.grid(row=1, column=2, sticky=tk.W+tk.E)

buttonframe.pack(fill="x")

but7 = tk.Button(buttonframe, text="7", font=("Arial", 16))
but7.grid(row=2, column=0, sticky=tk.W+tk.E)

buttonframe.pack(fill="x")


but8 = tk.Button(buttonframe, text="8", font=("Arial", 16))
but8.grid(row=2, column=1, sticky=tk.W+tk.E)

buttonframe.pack(fill="x")


but9 = tk.Button(buttonframe, text="9", font=("Arial", 16))
but9.grid(row=2, column=2, sticky=tk.W+tk.E)

buttonframe.pack(fill="x")


buttonframe1 = tk.Frame(root)
buttonframe1.columnconfigure(0, weight=1)
buttonframe1.columnconfigure(1, weight=1)


plusi = tk.Button(buttonframe1, text="+", font=("Arial", 16))
plusi.grid(row=0, column=1, sticky=tk.W+tk.E)
buttonframe1.pack(fill="x")

minusi = tk.Button(buttonframe1, text="-", font=("Arial", 16))
minusi.grid(row=0, column=2, sticky=tk.E+tk.W)
buttonframe1.pack(fill="x")







root.mainloop()

