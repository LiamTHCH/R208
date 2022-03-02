
from cgi import test
from pickletools import read_uint1
from signal import pthread_kill


class Patisserie:
    __createur = "ratatouille"
    def __init__(self,poids=0,categorie=None):
        self.__poids = poids
        self.__categorie = categorie
    def getPoid(self):
        return self.__poids
    def getcategorie(self) -> list:
        return self.__categorie
    def setPoid(self,poid):
        self.__poids = poid
    def setCategorie(self,categorie):
        self.__categorie = categorie
    def __str__(self) -> str:
        return str(str(self.__poids) +";"+ str(self.__categorie))
    @staticmethod
    def get_categorie_autorise() -> list:
        return list(("gateau","tarte"))
    @classmethod
    def setCreateur(cls,crea):
        cls.__createur = crea
    def getCreateur(cls):
        return cls.__createur

    def __eq__(self, __o: object) -> bool:
        return self.__poids == __o.getPoid()

    def __add__(self, __o: object) -> object:
        if self.__categorie == __o.getcategorie():
            return Patisserie(self.__poids+__o.getPoid(),self.__categorie)
        else:
            return Patisserie(self.__poids+__o.getPoid())
