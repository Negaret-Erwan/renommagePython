# -- coding: utf-8 --
from ClassAction import *
class RENOMMAGE(ACTION):
    def __init__(self, nomDuRépertoire, règle):
        ACTION.__init__(self, nomDuRépertoire, règle)
        
    def Renommer(self):
        print("ok")
