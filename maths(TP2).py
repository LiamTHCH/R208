from math import *
class Point:
    def __init__(self,x,y):
        self.__x = x
        self.__y = y

    def set_position(self,x,y):
        self.__x = x
        self.__y = y   

    def set_x(self,x): 
        self.__x = x

    def set_x(self,y):
        self.__y = y

    def get_postion(self):
        return (self.__x,self.__y)
    
    def get_x(self):
        return self.__x

    def get_y(self):
        return self.__y

    def double_distance_coordonner(self,x,y):
        return sqrt(((self.__x-x)**2)+((self.__y-y)**2))
    
    def double_distance_Point(self,Point):
        return sqrt(((self.__x-Point.get_x())**2)+((self.__y-Point.get_y())**2))

class Cercle:
    def __init__(self,position=(0,0),rayon=0):
        self.__position = position
        self.__rayon = rayon
    def diametre(self):
        return self.__rayon*2
    def perimetre(self):
        return 2*pi*self.__rayon
    def surface(self):
        return pi*(self.__rayon**2)