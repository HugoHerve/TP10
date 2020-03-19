from Ingénieur import Ingenieur

class IngeSn(Ingenieur):
    def __init__(self, nom, prenom, salaire, id, anneedembauche, nbjourtravail, nbheureprojet, nbheuregestion, responsabilite):
        Ingenieur.__init__(self, nom, prenom, salaire, id, anneedembauche, nbjourtravail, nbheureprojet, nbheuregestion)
        self.__responsabilite = responsabilite

    def Afficher(self):
         print("[id=",self._id,"], Nom prénom :",self._nom,self._prenom,", Salaire :",self._salaire,", Statut Ingénieur SN, Année d'embauche :", self._anneedembauche,", Nombre de jours de travail :",self._nbjourtravail,"Nombre heure de projet :", self._nbheureprojet,", Nombre heures de gestion :",self._nbheuregestion,",Responsabilité",self.__responsabilite)
