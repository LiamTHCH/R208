class Voiture:
    def __init__(self, marque=None, modele=None, chevaux=None,couleur=None,option=[]):
        self.__marque=marque
        self.__modele=modele
        self.__chevaux=chevaux
        self.__couleur=couleur
        self.__option = option
    def get_marque(self):
        return self.__marque
    def get_modele(self):
        return self.__modele
    def get_chevaux(self):
        return self.__chevaux
    def get_couleur(self):
        return self.__couleur
    def get_option(self):
        return self.__option
    def set_marque(self,marque):
        self.__marque = marque
    def set_modele(self,modele):
        self.__modele = modele
    def set_chevaux(self,chevaux):
        self.__chevaux = chevaux
    def set_couleur(self,couleur):
        self.__couleur = couleur
    def set_option(self,option):
        self.__option = option
    def add_option(self,option):
        self.__option.append(option)
    def remove_option(self,option):
        self.__option.remove(option)
    def is_option_present(self, opt):
        return opt in self.__option
    def __str__(self):
        tempstr = ""
        tempstr = tempstr + self.__marque + ","
        tempstr = tempstr + self.__modele+ ","
        tempstr = tempstr + str(self.__chevaux)+ ","
        tempstr = tempstr + self.__couleur+ ","
        for item in self.__option:
            tempstr = tempstr + str(item)+ ","
        return tempstr
