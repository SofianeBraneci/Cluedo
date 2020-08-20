# -*- coding: utf-8 -*-
"""
Created on Tue Aug 18 22:28:42 2020

@author: hp
"""


class FeuilleEnquete:
    
    # True: coché, False: non devidé
    def __init__(self, suspects, armes, lieux):
        self.suspects = {}
        self.armes = {}
        self.lieux = {}
        
        for suspect in suspects:
            self.suspects[suspect] = False
        for arme in armes:
            self.armes[arme] = False
        for lieu in lieux:
            self.lieux[lieu] = False
            
    def update(self, cartes=[]):
        # 1er fois quand on termine de dist les carte
        # apres quand on fait des hipothéses
        for carte in cartes:
            if carte.type == 'suspect':
                self.suspects[carte.nom] = True
            if carte.type == 'arme':
                self.armes[carte.nom] = True
            if carte.type == 'lieu':
                self.lieux[carte.nom] = True
                
    def __str__(self):
        string  = 'Ca'
            