# -*- coding: utf-8 -*-
"""
Created on Tue Aug 18 22:20:06 2020

@author: hp
"""


class Hypothese:
    
    def __init__(self, suspect, arme, lieu):
        self.suspect = suspect
        self.arme = arme
        self.lieu = lieu
        
    
    def match_with_other_players_sheet(self, current_player, players):
        discovered = []
        # player dispose un feille d'enquette
        # parcourir cette feuille et retourner toute les cartes
        # qui ont éétaient deviner
        for player in players:
            if player != current_player:
                for suspect, checked in player.feuille.suspects.items():
                    if checked:
                        discovered.append(player.get_carte(suspect.nom))
                for arme, checked in player.feuille.armes.items():
                    if checked:
                        discovered.append(player.get_carte(arme.nom))
                for lieu, checked in player.feuille.lieux.items():
                    if checked:
                        discovered.append(player.get_carte(lieu.nom))
        current_player.feuille.update(discovered)
                    
        

class Secret:
    """Solution dec"""
    def __init__(self, suspect, arme, lieu):
        self.suspect = suspect
        self.arme = arme
        self.lieu = lieu
    def __repr__(self):
        return ' '.join([self.suspect, self.arme, self.lieu])
        
        
class Accusation:
    
    def __init__(self, suspect, arme, lieu):
        self.suspect = suspect
        self.arme = arme
        self.lieu = lieu
        
    def match_with_solution(self, secret):
        # si True alors gagnant sinon out
        return secret.suspect == self.suspect and self.arme == secret.arme and secret.lieu == self.lieu
        