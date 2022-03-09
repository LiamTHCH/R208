import random
import re


class Guerrier:
    def __init__(self,pseudo="",niveau=1) -> None:
        self.__niveau = niveau
        self.__pseudo = pseudo
        self.__vie = niveau
    def getHealth(self)-> int:
        return self.__vie
    def setHealth(self,vie):
        self.__vie = vie
    def getPseudo(self) -> str:
        return self.__pseudo
    def setPseudo(self,pseudo):
        if self.verif_pseudo(pseudo):
            self.__pseudo = pseudo
        else:
            raise TypeError("Pseudo Invalide")
    def getNiv(self) -> int:
        return self.__niveau
    def setNiv(self,niv):
        self.__niveau = niv

    @staticmethod
    def verif_pseudo(pseudo) -> bool:
        ps = re.compile("^guerrier_[a-z]+[0-9]*")
        m = ps.match(pseudo)
        if m :
            return True
        else:
            return False


    def attaque(self,__o: object):
        __o.setHealth(__o.getHealth()-self.__niveau)
    
    def soigner(self):
        self.__vie = self.__niveau

    def combat(self,__o: object):
        temp = random.randint(1,2)
        while True:
            if temp == 1:
                self.attaque(__o)
            else:
                __o.attaque(self)
            if self.getHealth() >= 0:
                return self.__pseudo
            elif __o.getHealth() >= 0:
                return self.__pseudo
    
    