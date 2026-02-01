from tkinter import *
from Gestion.Gestion_fichier import *

def partie(gestion:Gestion_joueur, joueur1:str, joueur2:str):

    def victoire():
        resultat('1')

    def defaite():
        resultat('0')

    def nul():
        resultat('0.5')

    def resultat(resultat_j1:str):

        if resultat_j1 == '1':
            gestion.modification_elo(joueur1, joueur2, True)
            gestion.modification_elo(joueur2, joueur1, False)

        if resultat_j1 == '0':
            gestion.modification_elo(joueur1, joueur2, False)
            gestion.modification_elo(joueur2, joueur1, True)

        win.destroy()

    win = Tk()

    Label(win, text=f"{joueur1} ({gestion.list_joueur.get(joueur1)})", bg='green').pack(side=LEFT, padx=10)
    Label(win, text=f"{joueur2} ({gestion.list_joueur.get(joueur2)})", bg='green').pack(side=RIGHT, padx=10)

    Button(win, text="1-0", command=victoire).pack(pady=10)
    Button(win, text="0-1", command=defaite).pack(pady=10)
    Button(win, text="nul", command=nul).pack(pady=10)

    win.mainloop()