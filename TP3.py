import playsound
import random
import re


class Guerrier:
    def __init__(self,pseudo="",niveau=1,artefact=0) -> None:
        self.__niveau = niveau
        self.__pseudo = pseudo
        self.__vie = niveau
        self.__artefacte = artefact
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

    def getArte(self) -> int:
        return self.__artefacte
    def setArte(self,arte):
        self.__artefacte = arte

    @staticmethod
    def verif_pseudo(pseudo) -> bool:
        ps = re.compile("^guerrier_[a-z]+[0-9]*")
        m = ps.match(pseudo)
        if m :
            return True
        else:
            return False


    def attaque(self,__o: object):
        __o.setHealth(__o.getHealth()-((self.__niveau)*(1+((self.__artefacte/100)*random.randint(1,self.__artefacte)))))
    
    def soigner(self):
        self.__vie = self.__niveau

    def combat(self,__o: object):
        temp = random.randint(1,2)
        at = True
        while True:
            if temp == 1 and at:
                self.attaque(__o)
                at = False
            else:
                __o.attaque(self)
                at = True
            if self.getHealth() <= 0:
                return self.__pseudo
            elif __o.getHealth() <= 0:
                return self.__pseudo


class Joueur:
    def __init__(self,nom="",add="",guerrier=[]) -> None:
        self.__nom = nom
        if Joueur.verif_mail(add):
            self.__add = add
        else:
            raise TypeError("Addresse Mail invalide")
        self.__guerrier = guerrier
    
    def verif_mail(mail) -> bool:
        ps = re.compile("^[aA-zZ]+.+[aA-zZ]+@uha.fr$")
        m = ps.match(mail)
        if m :
            return True
        else:
            return False

    def ajout_guerrier(self, guerrier: object):
        self.__guerrier.append(guerrier)

    def set_guerrier_propriete(self, idx, pseudo, niveau, artefact):
        try:
            self.__guerrier[idx].setPseudo(pseudo)
            self.__guerrier[idx].setNiv(niveau)
            self.__guerrier[idx].setArte(artefact)

        except IndexError:
            print("Guerrier inexistant")
    def getGuerrier(self,idx):
        return self.__guerrier[idx]

    def tri_guerier(self):
        self.__guerrier =  sorted(self.__guerrier, key=lambda x: x.getNiv(), reverse=True)

    def tous_guerriers_morts(self):
        for item in self.__guerrier:
            if item.getHealth() <= 0:
                pass
            else:
                return False
        return True

    def simuler_combat(self,__o : object):
        ttself = 0
        ttother = 0
        for item in self.__guerrier:
            ttself = ttself + item.getNiv()
        
        for item in __o.__guerrier:
            ttother = ttother + item.getNiv()
        
        if ttself > ttother:
            return True
        else:
            return False

    def combat(self,other):
        counterself = 0
        counterother = 0
        while not self.tous_guerriers_morts() or not other.tous_guerriers_morts():
            playsound("round.mp3")
            if self.__guerrier[counterself].combat(other.getGuerrier(counterother)) == self.__guerrier[counterself].getPseudo():
                counterother = counterother + 1
            else:
                counterself = counterself + 1
        if self.tous_guerriers_morts():
            return 0
        else:
            playsound("victoire.mp3")