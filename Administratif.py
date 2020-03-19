from Employé import (Employe)


class Administratif(Employe):
    def __init__(self,nom, prenom, salaire, id, anneedembauche, nbjourtravail, servicedetravail):
         Employe.__init__(self,nom, prenom, salaire, id, anneedembauche, nbjourtravail)
         self.__servicedetravail = servicedetravail

    def Afficher(self):
        print("[id=",self._id,"], Nom prénom :",self._nom,self._prenom,", Salaire :",self._salaire,", Statut Administratif, Année d'embauche :", self._anneedembauche,", Nombre de jours de travail :",self._nbjourtravail,"Service : ",self.__servicedetravail)
