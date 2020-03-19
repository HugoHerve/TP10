from Salarié import Salarie

class Directeur(Salarie):
    def __init__(self, nom, prenom, salaire, id, anneedenomi):
        Salarie.__init__(self, nom, prenom, salaire, id)
        self.__anneedenomi = anneedenomi


    def Afficher(self):
        print("[",self._id,"]","Nom et prénom :",self._nom,self._prenom,"Salaire",self._salaire,"Statut : Directeur, Année de nomination:",self.__anneedenomi)
