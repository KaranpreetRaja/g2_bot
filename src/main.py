# import tkinter as tk
# from tkinter import ttk

# app = tk.Tk()
# app.title("Search Engine")
# search_prompt = tk.Label(app, text="Please Enter Search Query")
# search_prompt.grid(column=0, row=0)

# search_box = tk.Entry(app, width=20)
# search_box.grid(column=0, row=1)

# def search_clicked():
#     pass

# search_button = tk.Button(app, text="Search!", command=search_clicked)
# search_button.grid(column=1, row=1)

# app.geometry('350x200')


# app.mainloop()




import customtkinter

customtkinter.set_appearance_mode("System")  # Modes: system (default), light, dark
customtkinter.set_default_color_theme("blue")  # Themes: blue (default), dark-blue, green

app = customtkinter.CTk()  # create customtkinter window like you do with the Tk window
app.title("Search Engine")
app.geometry("400x240")



def button_function():
    print("button pressed")


def upload_action(event=None):
    filename = customtkinter.filedialog.askopenfilename()
    print(f'Selected {filename}')


# Use customtkinterButton instead of tkinter Button
search_button = customtkinter.CTkButton(app, text="Submit", command=button_function)

# label for search box
search_label = customtkinter.CTkLabel(app, text="Please Enter Search Query Below")

# search box
search_box = customtkinter.CTkEntry(app, width=150)

blank_label = customtkinter.CTkLabel(app, text="")

store_selection_label = customtkinter.CTkLabel(app, text="Please choose how you would like to store your selection")

def switch_event():
    print("switch toggled, current value:", switch_var.get())

switch_var = customtkinter.StringVar(value="on")
switch = customtkinter.CTkSwitch(app, text="customtkinterSwitch", command=switch_event, variable=switch_var, onvalue="on", offvalue="off")

def segmented_button_callback(value):
    if segemented_button_var.get() == "Create New CSV":
        upload_button.grid(column=0, row=6)

    elif(segemented_button_var.get() == "Append to Existing CSV"):
        pass

    else:
        upload_button.place_forget()

segemented_button_var = customtkinter.StringVar(value="Create New CSV")
segemented_button = customtkinter.CTkSegmentedButton(app, values=["Create New CSV", "Append to Existing CSV"], command=segmented_button_callback, variable=segemented_button_var)

upload_button = customtkinter.CTkButton(app, text="Upload", command=upload_action)

search_label.grid(column=0, row=0)
search_box.grid(column=0, row=1)

blank_label.grid(column=0, row=2)
store_selection_label.grid(column=0, row=3)
segemented_button.grid(column=0, row=4)
blank_label.grid(column=0, row=5)
upload_button.grid(column=0, row=6)
blank_label.grid(column=0, row=7)
search_button.grid(column=0, row=8)
# button.place(relx=0.5, rely=0.5, anchor=customtkinter.CENTER)
# switch.place(relx=0.5, rely=0.6, anchor=customtkinter.CENTER)
# segemented_button.place(relx=0.5, rely=0.7, anchor=customtkinter.CENTER)
# upload_button.place(relx=0.5, rely=0.8, anchor=customtkinter.CENTER)

app.mainloop()

