from tkinter import *
from InterfaceGraphique.Enregistrement import *

win = Tk()

# nouvelle partie

def nom_joueur():
    nom1 = joueur.get()
    nom2 = joueur2.get()
    recup_joueur(nom1, nom2, win)

partie_frame = Frame(win, bg='green')
partie_frame.pack(side=TOP)

partie_frame_top = Frame(partie_frame, bg='green')
partie_frame_top.pack(side=TOP)

partie_frame_bottom = Frame(partie_frame, bg='green')
partie_frame_bottom.pack(side=BOTTOM)

text = StringVar()
text.set("Nom Joueur")
joueur = Entry(partie_frame_bottom, textvariable=text)
joueur.pack(padx=10, pady=5, side=LEFT)

text2 = StringVar()
text2.set("Nom Joueur")
joueur2 = Entry(partie_frame_bottom, textvariable=text2)
joueur2.pack(padx=10, pady=5, side=RIGHT)

partie_label = Label(partie_frame_top, text="Nouvelle partie", bg='green')
partie_label.pack(side=TOP, pady=20, padx=10)

partie_label2 = Label(partie_frame_bottom, text="contre", bg='green')
partie_label2.pack()

valider_bouton = Button(partie_frame_top, text="valider", command=nom_joueur)
valider_bouton.pack(side=BOTTOM)

# barre d'outils

barre = Menu(win)

onglet = Menu(barre, tearoff=0)
onglet.add_command(label="Sauvegarder", command=sauvegarde)
barre.add_cascade(label="Fichier", menu=onglet)

win.config(menu=barre)

win.mainloop()