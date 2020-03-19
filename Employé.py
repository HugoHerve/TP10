from Salarié import Salarie

class Employe(Salarie):
    def __init__(self, nom, prenom, salaire, id, anneedembauche, nbjourtravail):
        Salarie.__init__(self, nom, prenom, salaire, id)
        self._anneedembauche = anneedembauche
        self._nbjourtravail = nbjourtravail

    def Afficher(self):
        pass
