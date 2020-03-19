from Multinationale import *
from Filiale import *
from Directeur import *
from Administratif import *
from IngéJr import *
from IngéSn import *


multi1 = Multinationale("RCAT","France")
FilialeBel = Filiale("RCAT-Belgique","Belgique",1990)
FilialeMar = Filiale("RCAT-Maroc", "Maroc", 1995)
FilialeTun = Filiale("RCAT-Tunisie","Tunisie", 1995)
FilialeAng = Filiale("RCAT-Angleterre","Angleterre", 2000)
DirecteurTunisie = Directeur("Raphael","Louyot","1250","4455","1990")
AdministratifTunisie = Administratif("Morineau","Quentin","1348","1333","1990","4","Comptabilité")
IngenieurSNTunisie = IngeSn("Brisard","Fantin","1900","2344","1990","4","23","34","3")
IngenieurJuniorBelgique = IngeJr("Ascouet","Martin","2343","2443","2000","3","34","67","2")
AdministratifBelgique = Administratif("Planquette","Léo","3444","9999","2222","34","Entretien")
IngenieurSNMaroc = IngeSn("Drapier","Louis","2333","4567","2134","32","45","1","OUI")
FilialeTun.addSalaries(DirecteurTunisie)
FilialeTun.addSalaries(AdministratifTunisie)
FilialeBel.addSalaries(IngenieurJuniorBelgique)
FilialeBel.addSalaries(AdministratifBelgique)
FilialeMar.addSalaries(IngenieurSNMaroc)
multi1.ajoutFiliale(FilialeMar)
multi1.ajoutFiliale(FilialeBel)
multi1.ajoutFiliale(FilialeTun)
multi1.ajoutFiliale(FilialeAng)
multi1.Afficher()
