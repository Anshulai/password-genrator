from tkinter import *
import string
import random
import pyperclip

def generator():
    password_length = int(length_Box.get())
    password = ''.join(random.sample(password_chars[choice.get()], password_length))
    passwordField.delete(0, END)
    passwordField.insert(0, password)
def copy():
    try:
        pyperclip.copy(passwordField.get())
    except Exception as e:
        print(f"Error copying password: {e}")

root = Tk()
root.config(bg='gray20')
root.title("Password Generator")
root.geometry("300x300")

choice = IntVar()
Font = ('arial', 13, 'bold')

password_chars = {
    1: string.ascii_lowercase,
    2: string.ascii_letters,
    3: string.ascii_letters + string.digits + string.punctuation
}

passwordLabel = Label(root, text='Password Generator', font=('times new roman', 20, 'bold'), bg='gray20', fg='white')
passwordLabel.grid(row=0, column=0, columnspan=2, pady=10)

weakradioButton = Radiobutton(root, text='Weak', value=1, variable=choice, font=Font)
weakradioButton.grid(row=1, column=0, pady=5)

mediumradioButton = Radiobutton(root, text='Medium', value=2, variable=choice, font=Font)
mediumradioButton.grid(row=1, column=1, pady=5)

strongradioButton = Radiobutton(root, text='Strong', value=3, variable=choice, font=Font)
strongradioButton.grid(row=2, column=0, columnspan=2, pady=5)

lengthLabel = Label(root, text='Password Length', font=Font, bg='gray20', fg='white')
lengthLabel.grid(row=3, column=0, pady=5)

length_Box = Spinbox(root, from_=5, to_=18, width=5, font=Font)
length_Box.grid(row=3, column=1, pady=5)

generateButton = Button(root, text='Generate', font=Font, command=generator)
generateButton.grid(row=4, column=0, columnspan=2, pady=5)

passwordField = Entry(root, width=25, bd=2, font=Font)
passwordField.grid(row=5, column=0, columnspan=2)

copyButton = Button(root, text='Copy', font=Font, command=copy)
copyButton.grid(row=6, column=0, columnspan=2, pady=5)

root.mainloop()