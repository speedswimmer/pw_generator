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
root.title('Password Gen')

root.minsize(250, 150)
root.maxsize(350, 250)

frame = ttk.Frame(root)
frame.config(width=250, height=200)
frame.config(relief=RIDGE)
frame.pack()

label = ttk.LabelFrame(frame, height = 100, width = 200, text = '...Click Create!')
label.config(relief = RIDGE, padding = (20, 15))
label.pack()
res_screen = ttk

text = Text(label, height=5, width = 20)
text.pack()

button = ttk.Button(root, text ='Create Password', command=callback)

number = IntVar()
number.set(8)
combo = ttk.Combobox(root, textvariable = number)
combo.config(values = (8,10,16))
combo.config(background="grey")
combo.pack()
button.pack()

root.mainloop()
