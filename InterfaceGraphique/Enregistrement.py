from tkinter import *
from Gestion.Gestion_joueur import *

gestion = Gestion_joueur()

def enregistrement():
    win = Tk()

    def envoyer():
        nom_joueur = joueur.get()
        gestion.enregistrement(nom_joueur)

    texte = StringVar()
    texte.set("Nom du joueur")
    joueur = Entry(win, textvariable=texte)
    joueur.pack()

    bouton = Button(win, text="enregistrer", command=envoyer)
    bouton.pack()

    win.mainloop()