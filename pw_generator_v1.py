import tkinter, time
import random, string

def end():
    main.destroy()

def randompassword():
    chars=string.ascii_uppercase + string.ascii_lowercase + string.digits
    size = 6
    return "".join(random.choice(chars) for x in range(size,20))

def zeigen():
    tx1.insert("end", randompassword())
    tx1.insert("end","\n")
    

#Untersuchung des Passwortes
def pwtest():
    eingabe = entry.get()
    if eingabe =="Bingo":
        lb["fg"]="green"
        lb["text"]="Zugang erlaubt!"
    else:
        lb["fg"]="red"
        lb["text"]="Zugang verweigert!"

main = tkinter.Tk()

main.label="Passwort"

#Text Widget configuration
tx1 = tkinter.Text(main)
tx1.config(state="normal", width=30, height=8, bg="#d3e5ff")
tx1.insert("end","...bitte auf Create klicken!\n")
tx1.pack()

btest=tkinter.Button(main,text="Create", command=zeigen).pack()

#Anzeigen des Ergebnisses
lb=tkinter.Label(main, text="Zugang")
lb.pack()

beende=tkinter.Button(main, text="End", command=end).pack()
main.mainloop()
