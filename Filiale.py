

class Filiale:
    def __init__(self, nom, pays, creation):
        self.__nom = nom
        self.__pays = pays
        self.__creation = creation
        self.__nbsalaries = []

    def addSalaries(self, element):
        self.__nbsalaries.append(element)
    def suppSalaries(self, element):
        self.__nbsalaries.remove(element)

    def getDate(self):
        return self.__creation
    def getNom(self):
        return self.__nom
    def getNbSalar(self):
        return len(self.__nbsalaries)
    def getList(self):
        return self.__nbsalaries



