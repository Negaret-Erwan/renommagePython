# -- coding: utf-8 --
from ClassRègle.py import *
import ConfigParser

class LISTEREGLE:
    def __init__(self, règles=[]):
        self.règles=règles

    def Get_règles(self):
	règle=""
        for r in self.règles:
            règle=règle+r.__str__()+"\n"
            
    def Set_règles(self, règles):
        self.règles.append(règles)
        
    def Charger(self, nomFichier):
	with open('renommage.ini', 'r') as file:
	    file.read()
	    
    def Sauvegarder(slef, nomFichier):
	with open('renommage.ini', 'w') as file:
	    file.write('letexte')
