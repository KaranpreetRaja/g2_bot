import tkinter as tk
from tkinter import ttk

window = tk.Tk()
window.title("Search Engine")
search_prompt = tk.Label(window, text="Please Enter Search Query")
search_prompt.grid(column=0, row=0)

search_box = tk.Entry(window, width=20)
search_box.grid(column=0, row=1)

def search_clicked():
    pass

search_button = tk.Button(window, text="Search!", command=search_clicked)
search_button.grid(column=1, row=1)

window.geometry('350x200')


window.mainloop()
