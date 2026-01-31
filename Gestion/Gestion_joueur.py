from Gestion.Calcul import calcul

class Gestion_joueur:

    def __init__(self):
        self.list_joueur = {}

    def enregistrement(self, nom_joueur:str):
        file = open('joueur.txt', 'a+')
        file.write(f'{nom_joueur}:1000\n')
        self.list_joueur[nom_joueur] = 1000.0
        file.close()

    def start(self):
        file = open('joueur.txt', 'r+')

        for line in file.readlines():
            line = line.replace('\n', '')
            element = line.split(':')
            self.list_joueur[element[0]] = float(element[1])

        file.close()

    def modification_elo(self, nom_joueur:str, joueur_adverse:str, victoire:bin):
        elo_joueur = self.list_joueur.get(nom_joueur)
        elo_adverse = self.list_joueur.get(joueur_adverse)

        point = calcul(elo_joueur, elo_adverse)

        if victoire:
            self.list_joueur[nom_joueur] = elo_joueur + point

        if not victoire:
            self.list_joueur[nom_joueur] = elo_joueur - point

    def validation_modification(self):
        file = open('joueur.txt', 'w')
        file.close()
        file = open('joueur.txt', 'a')

        for cle in self.list_joueur.keys():
            texte = f'{cle}:{self.list_joueur.get(cle)}\n'
            file.write(texte)

        file.close()