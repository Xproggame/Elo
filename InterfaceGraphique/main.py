from tkinter import *
from InterfaceGraphique.Enregistrement import *

win = Tk()

frame = Frame(win, bg='green')
frame.pack(side=TOP)

text = StringVar()
text.set("Nom Joueur")
joueur = Entry(frame, textvariable=text)
joueur.pack()

win.mainloop()