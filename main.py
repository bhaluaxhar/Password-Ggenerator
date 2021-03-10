from tkinter import messagebox
from tkinter import *
from random import randint

root = Tk()
root.title("Password Generator by Axhar")
root.geometry("571x300")
# root.protocol("WM_DELETE_WINDOW", exit_window)
# root.wm_attributes('-alpha', 0.6)

# Background Image
f = PhotoImage(file="password.png")
background_label = Label(root, image=f)
background_label.place(x=0, y=0, relwidth=1, relheight=1)


def password():
    # delete entry box if clicked more than one
    show.delete(0, END)
    # get password length from get_length using new variable
    pw_length = int(get_length.get())

    # -------------------------------Working on error if entry box is empty---------------#
    if int(get_length.get()) == 0:
        messagebox.showerror("Entry Error", "Your length should be atleast 1")
    else:
        pass
    # -------------------------------Working on error if entry box is empty---------------#
    # variable to save password
    my_password = ''
    # loop to control length of password
    for x in range(pw_length):
        my_password += chr(randint(33, 126))
    # show password
    show.insert(0, my_password)


def copy():
    # first clear a clipboard
    root.clipboard_clear()
    # copy to clipboard
    root.clipboard_append(show.get())
    messagebox.showinfo("Status", "Copied to Clipboard")


# text box
msg = Label(root, text="Enter Length of password", font=("Helvetica 40 bold", 13), bd=0, fg="#0d1d30", bg='#6497cb')
msg.pack(pady=3)
# Frame for Label
Label = LabelFrame(root, text="Enter password Length", bd=0, bg='#41cbf2')
Label.pack(pady=20)

# Entry box to get length of password
get_length = Entry(root, font=("Verdana 10 bold", 20), bd=0, bg='#41cbf2')
get_length.pack(pady=20, padx=20)

# Entry box to show password

show = Entry(root, text='', font=("Verdana 10 bold", 20), bd=0, bg="#41cbf2")
show.pack(pady=20)

# Frame for buttons

button_Frame = Frame(root, bg='#41cbf2')
button_Frame.pack(pady=20)

# create buttons
generate_button = Button(root, text='Generate password', command=password, bd=5, fg="#0d1d30", bg='#2899dd')
generate_button.place(relx=1, x=-350, y=250, anchor=NE, )

copy_button = Button(root, text='Copy to Clipboard', command=copy, bd=5, fg="#0d1d30", bg='#2899dd')
copy_button.place(relx=1, x=-100, y=250, anchor=NE)

mainloop()
