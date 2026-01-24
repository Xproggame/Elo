class Gestion_joueur:

    def __init__(self):
        self.list_joueur = {}

    def enregistrement(self, nom_joueur:str):
        file = open('joueur.txt', 'a+')
        file.write(f'{nom_joueur}:1000\n')
        file.close()

    def start(self):
        file = open('joueur.txt', 'r+')

        for line in file.read():
            line = line.replace('\n', '')
            element = line.split(':')
            self.list_joueur[element[0]] = float(element[1])

        file.close()