from Ingénieur import Ingenieur

class IngeJr(Ingenieur):
    def __init__(self, nom, prenom, salaire, id, anneedembauche, nbjourdetravail, nbheuredeprojet, nbheuregestion, anneedexperience):
        Ingenieur.__init__(self, nom, prenom, salaire, id, anneedembauche, nbjourdetravail, nbheuredeprojet, nbheuregestion)
        self.__anneedexperience = anneedexperience

    def Afficher(self):
        print("[",self._id,"], Nom prénom :",self._nom,self._prenom,", Salaire :",self._salaire,", Statut Ingénieur Jr, Année d'embauche :", self._anneedembauche,", Nombre de jours de travail :",self._nbjourtravail,"Nombre heure de projet :", self._nbheureprojet,", Nombre heures de gestion :",self._nbheuregestion,",Années d'expérience",self.__anneedexperience)
