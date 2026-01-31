from tkinter import *
from tkinter.messagebox import askyesno
from Gestion.Gestion_joueur import *
from InterfaceGraphique.Partie import *

gestion = Gestion_joueur()

def enregistrement(win:Tk, joueur:str):

    def envoyer():
        nom_joueur = joueur
        gestion.enregistrement(nom_joueur)

    if askyesno("Nouveau joueur", f"Le joueur {joueur} n'existe pas. Voulez vous l'enregistrer ?"):
        envoyer()

def rechercher_joueur(nom_joueur:str):

    for joueur in gestion.list_joueur.keys():

        if joueur == nom_joueur:
            return True

    return False

def recup_joueur(joueur1:str, joueur2:str, win:Tk):

    if gestion.list_joueur == {}:
        gestion.start()

    if rechercher_joueur(joueur1):

        if rechercher_joueur(joueur2):
            partie(gestion, joueur1, joueur2)

        else:
            enregistrement(win, joueur2)
            partie(gestion, joueur1, joueur2)

    elif rechercher_joueur(joueur2):
        enregistrement(win, joueur1)
        partie(gestion, joueur1, joueur2)

    else:
        enregistrement(win, joueur1)
        enregistrement(win, joueur2)
        partie(gestion, joueur1, joueur2)