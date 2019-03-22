#PW Generator v1.2
from tkinter import *
from tkinter import ttk
import string
import random

def callback():
    label.config(text = 'Password Results:')
    randompassword()

def randompassword():
    text.delete('1.0','end')
    for x in range (4):
        chars=string.ascii_uppercase + string.ascii_lowercase + string.digits
        text.insert('end', ''.join(random.choice(chars) for x in range(number.get())))
        text.insert('end','\n')

root = Tk()
root.title('Password Reactor')

root.minsize(280, 190)
root.maxsize(350, 250)

frame = ttk.Frame(root)
frame.config(width=250, height=200)
frame.config(relief=RIDGE)
frame.pack()

label = ttk.LabelFrame(frame, height = 100, width = 200, text = '...Click Create!')
label.config(relief = RIDGE, padding = (20, 15))
label.pack()

text = Text(label, height=5, width = 20)
text.pack()

footer = ttk.Frame(root)
footer.pack()

number = IntVar()
number.set(10)

combo = ttk.Combobox(footer, width = 4, textvariable = number)
combo.config(values = (8,10,16,18))

comlabel = ttk.Label(footer, text = 'Number of digits: ')
comlabel.grid(column = 0, row = 1, sticky="e")
combo.grid(column = 1, row = 1, sticky="w")

button = ttk.Button(footer, text ='Create Passwords', command = callback)
button.grid(column = 0, row = 2, columnspan = 2)

root.mainloop()
