class Multinationale:
    def __init__(self, nom, paysorigine):
        self.__nom = nom
        self.__paysOrigine = paysorigine
        self.__filiales = []

    def ajoutFiliale(self, element):
        self.__filiales.append(element)

    def Afficher(self):
        print("La multinationale",self.__nom,"est composée de",len(self.__filiales),"filiale(s). Son pays d'origine est la/le",self.__paysOrigine,".")
        Daterefe = 3000
        plusancienne = 0
        nbsalaireplusancinne = 0
        for i in self.__filiales:
            if i.getDate()< Daterefe:
                Daterefe = i.getDate()
                plusancienne = i.getNom()
                nbsalaireplusancinne = i.getNbSalar()
        print("La filiale la plus ancienne est",plusancienne,". Elle est composée de :",nbsalaireplusancinne,'salarié(s)' )
        nbsalariestotal = 0
        for e in self.__filiales:
            nbsalariestotal += e.getNbSalar()
        print(self.__nom,"est composée d'un total de",nbsalariestotal,'salarié(s)')
        for i in self.__filiales:
            for j in i.getList():
                j.Afficher()




        #if (len(self.__nbsalaries)== 0):
        #    print("La filiale",self.__nom,"est composée de 0 salariés")
        #else:
        #    print("La filiale", self.__nom,'est composée de', len(self.__nbsalaries),"salarié(s)")
        #    for i in self.__nbsalaries:
        #        i.Afficher()
