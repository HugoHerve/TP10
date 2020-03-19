from Employé import Employe

class Ingenieur(Employe):
    def __init__(self, nom, prenom, salaire, id, anneedemauche, nbjourtravail, nbheureprojet, nbheuregestion):
        Employe.__init__(self, nom, prenom, salaire, id, anneedemauche, nbjourtravail)
        self._nbheureprojet = nbheureprojet
        self._nbheuregestion = nbheuregestion

    def Afficher(self):
        pass
